from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages

from store.forms import CustomUserForm

def registerpage(request):
    form = CustomUserForm()
    if request.method == 'POST':
       form = CustomUserForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request,"Registered Successfully! Login to continue")
           return redirect("/login") 
    context = {'form':form}
    return render(request,"store/auth/register.html",context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in.")
        return redirect('/')
    else:
        if request.method == 'POST':
            _username = request.POST.get('username')
            _password = request.POST.get('password')
            
            user = authenticate(request, username=_username, password=_password)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Succesfully.")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password.")
                return redirect("/login")
        
        return render(request,"store/auth/login.html")
    
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
    return redirect('/')
    