from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path('userSignup',views.UserSignup,name='userSignup'),
    path('hotelSignup',views.HotelSignup,name='hotelSignup'),
    path('login',views.login,name='login'),
    path('userprofileupdate',views.updateUserProfile,name='userprofileupdate'),
    path('hotelprofileupdate',views.updateHotelProfile,name='hotelprofileupdate')
]
