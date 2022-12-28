from datetime import datetime, date, timedelta
from rest_framework import serializers
from hashid_field.rest import HashidSerializerCharField
from .models import BookTransaction


class BookingSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(source_field="order.OrderHeader.id", read_only=True)
    member = serializers.SerializerMethodField()
    return_date = serializers.SerializerMethodField()

    class Meta:
        model = BookTransaction
        fields = ("id", "booking_no", "booking_date", "member", "user_id", "status")
        extra_kwargs = {
            "user_id": {"write_only": True},
        }

    def get_return_date(self, obj):
        borrowing = BookTransaction.booking_date
        return_date = BookTransaction.booking_date + timedelta(days=30)
        return float(return_date)

    def get_member(self, obj):
        try:
            return {
                "id": str(obj.member_id.id),
                "name": "{} {}".format(
                    obj.member_id.first_name, obj.member_id.last_name
                ),
            }
        except Exception:
            return ""
