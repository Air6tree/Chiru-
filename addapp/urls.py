from django.urls import re_path
from . import views 
from . import views

urlpatterns = [
  re_path(r'^$',views.display),
  re_path(r'^sum$',views.show),
]