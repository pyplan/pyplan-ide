from rest_framework import pagination

class UserPagination(pagination.PageNumberPagination):
    page_size = 1000
