from rest_framework import pagination


class MyPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return {
            "content": data,
            "pagination": {
                "limit": self.page.paginator.per_page,
                "total_page": self.page.paginator.num_pages,
                "total_rows": self.page.paginator.count,
                "current_page": self.page.number,
            },
        }
