from rest_framework import pagination


class PaginacaoFeira(pagination.PageNumberPagination):
    page_size = 5
    page_query_param = 'pagina'
    page_size_query_param = 'reg_pagina'
    max_page_size = 10

