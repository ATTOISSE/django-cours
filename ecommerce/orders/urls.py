from django.urls import path
from .views import hello,index,get_client
from .views import client_info,HomeView

urlpatterns = [
    path('hello/',hello),
    path('order-info/<int:id>/',client_info),
    path('test/',HomeView.as_view()),
    path('home/',index,name='home'),
    path('catalog/<int:id>',get_client,name='catalog'),
]
