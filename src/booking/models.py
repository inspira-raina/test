from django.db import models
from hashid_field import HashidAutoField
from django.contrib.auth.models import User
from src.book.models import Book

# Create your models here.
class BookTransaction(models.Model):
    class Meta:
        db_table = "book_transactions"

    ON_GOING = "ON_GOING"
    RETURNED = "RETURNED"
    OVERDUE = "OVERDUE"
    STATUS_CHOICES = (
        (ON_GOING, "On Going"),
        (RETURNED, "Returned"),
        (OVERDUE, "Overdue"),
    )

    id = HashidAutoField(primary_key=True)
    booking_no = models.CharField(max_length=10)
    booking_date = models.DateTimeField(blank=True, null=True)
    user_id = models.ForeignKey(
        User,
        db_column="user_id",
        related_name="%(class)s_user_id",
        on_delete=models.PROTECT,
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ON_GOING)

    def __str__(self):
        return "%s" % (self.id)


class TransactionItem(models.Model):
    class Meta:
        db_table = "transaction_items"

    id = HashidAutoField(primary_key=True)
    book_transactions_id = models.ForeignKey(
        BookTransaction,
        db_column="book_transactions_id",
        related_name="%(class)s_book_transactions_id",
        on_delete=models.PROTECT,
    )
    book_id = models.ForeignKey(
        Book,
        db_column="book_id",
        related_name="%(class)s_book_id",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return "%s" % (self.id)
