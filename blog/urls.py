from django.urls import path

from blog import views

urlpatterns = [
    path("", views.get_main_page, name="main_page"),
    path("<int:pk>/", views.get_detail_blog, name="detail"),
]