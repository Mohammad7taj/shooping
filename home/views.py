from django.shortcuts import render


def home(request):
    return render(request, "home/home.html")



def home2(request):
    return render(request, "home/home2.html")