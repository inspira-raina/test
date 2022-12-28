from django.contrib import admin
from .models import BookTransaction, TransactionItem

# Register your models here.
admin.site.register(BookTransaction)
admin.site.register(TransactionItem)
