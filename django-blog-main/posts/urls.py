from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post'),
    
    # 🟢 ADD THIS ROUTE FOR YOUR CUSTOM ADMIN PANEL:
    path('admin-panel/new/', views.create_post, name='create_post'),
]
