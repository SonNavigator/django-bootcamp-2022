from django.urls import path
from .views import index, single_post, contact


urlpatterns = [
    # path('url name', function)
    path("", index, name="home"),
    path("posts/<int:id>", single_post),
    path("contact-us", contact, name="contact"),

]
