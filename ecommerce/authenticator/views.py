from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            print(user)
            login(request,user)
            messages.success(request,"l'utilisateur est enregistré avec succés !!! ",extra_tags='success')
            return redirect('home')
        else:
            messages.error(request,"les données soumises sont invalide !!! ",extra_tags='danger')
            return redirect('register')

    else:
        form = UserCreationForm()
    return render(request,'authenticator/register.html',{'form':form})

def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"l'utilisateur est bien connecté avec succés !!! ")
                return redirect('home')
            else:
                messages.error(request,"error de connection !!! ")

    else:
        form = AuthenticationForm()
    return render(request,'authenticator/connection.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')