from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("main", views.main, name="main"),
    path("blog", views.blog, name="blog"),
    path("order", views.order, name="order"),
    path("plan", views.plan, name="plan"),
    path("products", views.products, name="products"),
    path("account", views.account, name="account"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logoutUser, name="logout"),
]