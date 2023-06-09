from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model,login,logout,authenticate
from .models import Agent
from location.models import Apartment
# Create your views here.
User=get_user_model()
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email = request.POST.get('email')
        number= request.POST.get('number')
        user=User.objects.create_user(username=username,password=password,email=email,phone_number=number)
        login(request,user)
        return redirect('index')

    return render(request,'location/signup.html')

def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user:
            login(request,user)
            return redirect('index')

    return render(request,'location/login.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def agent(request, variable):
    if variable=="grid":
        return render(request, f"location/agents-grid.html",context={'agents':Agent.objects.all()})
    else:
        agent=get_object_or_404(Agent,slug=variable)
    return render(request, f"location/agent-single.html",context={'agent':agent,'apartments':Apartment.objects.filter(agent=agent.id)})