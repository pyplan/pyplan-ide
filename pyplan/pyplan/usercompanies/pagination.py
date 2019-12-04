from rest_framework import pagination

class UserCompaniesPagination(pagination.PageNumberPagination):
    page_size = 1000
