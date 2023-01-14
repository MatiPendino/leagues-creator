from django.urls import path
from apps.authentication import views

# auth/
urlpatterns = [
    path("signup", views.signup, name="register"),
    path("signin", views.signin, name="signin"),
    path("sign_out", views.sign_out, name="sign_out")
]