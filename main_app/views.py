from django.shortcuts import render

games = [
    {'name': 'Read Dead Redemption 2'}
]

# Create your views here.

def home(request):
    return render(request, 'home.html')