from django.urls import path
from . import views


urlpatterns=[
    path('api/register',views.register,name='register'),
    path('api/login',views.login,name='login'),
    path('api/contact',views.contacts,name='contacts'),
    path('api/twowheelerapi',views.twowheeler_list,name='twowheeler_list'),
    path('api/twowheeler/',views.twowheeler_detail,name='twowheeler_detail'),
    path('api/delete/<str:pk>/',views.delete,name='delete'),
    path('api/getdata/',views.getdata,name='getdata'),
    path('api/book/',views.viewbook,name='viewbook')
]