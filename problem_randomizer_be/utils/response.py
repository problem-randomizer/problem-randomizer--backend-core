from rest_framework.response import Response


class CustomResponse(Response):
    def __init__(self, status_code, message, data):
        super().__init__(status=status_code, data={"statusCode": status_code, "message": message, "data": data})
