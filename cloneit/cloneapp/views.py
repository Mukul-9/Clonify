from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .form import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def home(request):
	return render(request, 'cloneapp/home.html')

def signupuser(request):
	if request.method=='GET':
		return render(request, 'cloneapp/signupuser.html',{'form':RegisterForm()})
	else:	
		if request.POST['password']==request.POST['confirm_password']:
			user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'])
			user.save()
			login(request,user)
			return redirect('home')
		else:
			return render(request, 'cloneapp/signupuser.html',{'form':RegisterForm()})


@login_required
def logoutuser(request):
	if request.method=='POST':
		logout(request)
		return redirect('signupuser')


def loginuser(request):
	if request.method=='GET':
		return render(request, 'cloneapp/loginuser.html',{'form':AuthenticationForm()})
	else:
		user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
		if user is None:
			return render(request, 'cloneapp/loginuser.html',{'form':AuthenticationForm()})
		else:
			login(request,user)
			return redirect('home')

