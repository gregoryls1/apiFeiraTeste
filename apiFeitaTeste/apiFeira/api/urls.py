from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^feira$', FeiraList.as_view()),
]