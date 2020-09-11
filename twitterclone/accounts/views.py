from django.shortcuts import render,redirect
from . forms import RegisterForm
from django.contrib import messages
from .forms import ProfileUpdatedForm
from django.contrib.auth.decorators import login_required
# Create your views here
def register(request):
    if request.method=='post':
        form=RegisterForm(request.post)
        if form.is_valid():
            form.save()
            messages.success(request,f"Account Created")
            return redirect('login')
    else:
        form=RegisterForm()
    return render(request,'accounts/signup.html',{'form':form})
@login_required
def profile(request):
    return render(request,'accounts/profile.html')
def profileupdate(request):
    if request.method=='post':

        pform=ProfileUpdatedForm(request.POST,request.FILES,instance=request.user.profile)
        if pform.is_valid:
            pform.save()
            return redirect('profile')
    else:
        pform=ProfileUpdatedForm(instance=request.user.profile)
        
    return render(request,'accounts/profileupdate.html',{'pform':pform})