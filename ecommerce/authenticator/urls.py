from django.urls import path
from .views import signup_view,signin_view,logout_view

urlpatterns = [
    path('register/',signup_view,name='register'),
    path('connection/',signin_view,name='login'),
    path('logout/',logout_view,name='logout'),
]
