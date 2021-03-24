from rest_framework.pagination import PageNumberPagination


class PortPagination(PageNumberPagination):
    page_size = 5