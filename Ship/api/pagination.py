from rest_framework.pagination import PageNumberPagination


class ShipPagination(PageNumberPagination):
    page_size = 5