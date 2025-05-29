from django.urls import path
from .views import post_list_api  # ✅ now this works perfectly

urlpatterns = [
    path('api/posts/', post_list_api, name='post_list_api'),
]
