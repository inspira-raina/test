from django.contrib import admin
from .models import BookCategory, Book

# Register your models here.
admin.site.register(BookCategory)
admin.site.register(Book)
