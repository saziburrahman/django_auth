from django.shortcuts import render,redirect
from .models import user

# Create your views here.
def Home(request):
    return render(request,"index.html")

def login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        u=user(name=email)
        u.save()
        print(email)
        return redirect('/login')
    else:
        userList=user.objects.all()
        print("Users are")
        print(userList)
        return render(request,"login.html",{"users":userList})

def register(request):
    
    return render(request,"register.html")