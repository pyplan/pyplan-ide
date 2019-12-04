from rest_framework import pagination

class CompanyPagination(pagination.PageNumberPagination):
    page_size = 1000
