from rest_framework import status
from rest_framework.response import Response


def MyResponse(
    code=400, message="Success", data={}, header_status_code=status.HTTP_200_OK
):
    meta = {
        "error_schema": {
            "error_code": code,
            "error_message": message,
        }
    }

    data = {"output_schema": data}

    res = dict(meta, **data)

    return Response(res, status=header_status_code)
