# pagination.py (create this file in your app if needed)

from rest_framework.pagination import PageNumberPagination

class CustomProductPagination(PageNumberPagination):
    page_size = 2  # Default page size
    page_size_query_param = 'page_size'  # Allow user to override ?page_size=10
    max_page_size = 100  # Optional
