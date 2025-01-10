from django.shortcuts import render, redirect
from.forms import RegisterForm
from django.contrib import messages
from django.contrib import auth
# Create your views here.
def register(request):
    forms=RegisterForm()
    
    if request.method=='POST':
        forms=RegisterForm(request.POST)
        if forms.is_valid:
            forms.save()
            messages.success(request, 'success account created')
            return redirect('login')
        else:
            messages.warning(request, 'Error in creating account, try again')
            return redirect('register')
    context={
        'form':forms
    }
    return render(request, 'user/register.html', context)



def logout(request):
    auth.logout(request)
    messages.warning(request, 'you are logout, please login')
    return redirect('login')


def index(request):
    return render(request, 'social/index.html')