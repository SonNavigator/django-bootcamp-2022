from django.urls import path
from .views import index, single_post


urlpatterns = [
    # path('url name', function)
    path("", index),
    path("posts/<int:id>", single_post)
]
