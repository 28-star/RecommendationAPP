from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    return render(request,'login.html')
def UserSignup(request):
    return render(request,'userSignup.html')
def HotelSignup(request):
    return render(request,'hotelSignup.html')
def updateUserProfile(request):
    return render(request,'updateUserProfile.html')
def updateHotelProfile(request):
    return render(request,'updateHotelProfile.html')



