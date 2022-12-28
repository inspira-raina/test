# serializers.py
from rest_framework import serializers
from hashid_field.rest import HashidSerializerCharField
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(source_field="order.OrderHeader.id", read_only=True)
    category = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "category",
            "description",
            "number_of_copy",
            "created_at",
            "updated_at",
        )

    def get_category(self, obj):
        return {
            "id": str(obj.category_id.id),
            "name": obj.category_id.name,
        }
