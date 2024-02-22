from django.shortcuts import render,redirect
from fbapp.forms import userform
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from fbapp.models import user_data
from django.contrib.auth.decorators import login_required

# Index Page
def index(request):
    return render(request,"index.html")

# Main Page
@login_required(login_url='user_login')
def main(request):
    return render(request,"main.html")

# Delete Page
@login_required(login_url='user_login')
def delety(request):
    return render(request,"delete.html")

# logout Button
@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    return redirect('user_login')

# Coversation Page
@login_required(login_url='user_login')
def chat_page(request):
    return render(request,"chat.html")

# Register Page
def register(request):
    registered = False

    if request.method == 'POST':
        form = userform(request.POST)
        # form = request.POST.get('username')
        # form1 = request.POST.get('password')

        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            registered = True
    else:

        form = userform()

    return render(request,"user_register.html",{'form':form,'registered':registered})

# login page
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('main')
            else:
                return HttpResponse("user not active")
        else:
            return HttpResponse("<h1>invalid creds</h1>")
    return render(request,"user_login.html")

# ----------------------------------------------------------------------------

# # Welcome Page
# def welcome(request):
#     form1 = userform()

#     if request.method == 'POST':
#         form1 = userform(request.POST)

#         if form1.is_valid():
#             user = form1.save()
#             user.set_password(user.password)
#             user.save()

#     return render(request,"welcome.html",{'form1':form1})

# --------------------------------------------------------------------------

