from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "accounts"

# There is intentionally NO "register" / "signup" URL (FR-25).
# Admins are created with:  python manage.py createsuperuser
urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),   # POST only in Django 5
    path("dashboard/", views.dashboard, name="dashboard"),
]
