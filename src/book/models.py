from django import db
from django.db import models
from hashid_field import HashidAutoField

# Create your models here.
class BookCategory(models.Model):
    class Meta:
        db_table = "book_categories"

    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return "%s" % (self.id)


class Book(models.Model):
    class Meta:
        db_table = "books"

    id = HashidAutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    category_id = models.ForeignKey(
        BookCategory,
        db_column="category_id",
        related_name="%(class)s_category_id",
        on_delete=models.CASCADE,
    )
    description = models.TextField()
    number_of_copy = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return "%s" % (self.id)
