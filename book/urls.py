from django.urls import path

from book.views import RegisterView, LoginView

app_name = "book"
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]
