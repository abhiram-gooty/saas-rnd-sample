from django.contrib import admin
from django.urls import path
from .views import homePage,about_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',about_view),
    path('',homePage)
]
