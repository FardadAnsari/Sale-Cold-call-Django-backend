from django.urls import path
from . import views


urlpatterns = [
    path('', views.LoginUser.as_view(), name='user'),
    path('info/', views.InfoUser.as_view(), name='info-user'),

]