from django.urls import path
from .views import (
    index, single_post, contact, search, 
    sign_up, sign_out, sign_in
)


urlpatterns = [
    # path('url name', function)
    path("", index, name="home"),
    path("posts/<int:id>", single_post),
    path("contact-us", contact, name="contact"),
    path("search", search, name="search"),
    path("sign-up", sign_up, name="sign-up"),
    path("sign-out", sign_out, name="sign-out"),
    path("sign-in", sign_in, name="sign-in"),
]
