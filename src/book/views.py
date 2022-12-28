from django.conf import settings
from django.db.models import Q
from rest_framework import viewsets, permissions
from src.helper.response import MyResponse
from .serializers import BookCategorySerializer, BookSerializer
from .models import Book

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response


class BookViewSet(viewsets.ViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    # queryset = Book.objects.all()
    # serializer_class = BookSerializer

    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(user)
        return Response(serializer.data)

        # def list(self, request):
        limit = request.GET.get("limit", 10)
        sort = request.GET.get("sort", None)
        q = request.GET.get("q", None)

        # if limit:
        #     # Dynamic page_size
        #     self.pagination_class.page_size = limit

        """
        -- Start --
        Dynamic filter parameter queryset
        """
        args = Q()

        if q is not None:
            args = args | Q(title__icontains=q)

        """
        Dynamic filter parameter queryset
        -- End --
        """

        """
        -- Start --
        Dynamic sort parameter queryset
        """
        order_by = []

        if sort is not None:
            order_by = []

            # Get from filter
            split_sort = sort.split(",")

            for row in split_sort:
                split_row = row.split("~")

                try:
                    key = split_row[0]
                except IndexError:
                    key = None

                try:
                    value = split_row[1]
                except IndexError:
                    value = "DESC"

                order_by.append("-" + str(key) if value == "DESC" else str(key))
        else:
            order_by.append("-created_date")

        order_by.append("-id")
        """
        -- End --
        Dynamic sort parameter queryset
        """

        queryset = (
            self.filter_queryset(self.get_queryset())
            .filter(*(args,))
            .order_by(*order_by)
        )
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = self.get_paginated_response(serializer.data)
            return MyResponse(
                settings.RESPONSE_META["SUCCESS"]["CODE"],
                "",
                data,
            )

        serializer = self.get_serializer(queryset, many=True)
        data = {"content": serializer.data}
        return MyResponse(
            settings.RESPONSE_META["SUCCESS"]["CODE"],
            "",
            data,
        )
