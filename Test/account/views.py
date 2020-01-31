from django.shortcuts import render,HttpResponseRedirect
from .forms import *
from django import views
# Create your views here.
class UserRegistration(views.View):
    UserRegForm = UserRegistrationForm
    template_name = 'account/user_registration.html'

    def get(self,request,*args,**kwargs):
        form = self.UserRegForm()
        context = {'form':form}
        return render(request,self.template_name,context=context)

    def post(self,request,*args,**kwargs):
        form = self.UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/login/')
        return render(request,self.template_name,context={'form':form})

class UserLoginView(views.View):
    template_name = 'account/user_login.html'
    LoginForm = UserLoginForm

    def get(self,request,*args,**kwargs):
        form = self.LoginForm()
        return render(request,self.template_name,context={'form' : form})

    def post(self,request,*args,**kwargs):
        form = self.LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('Name')
            passwd = form.cleaned_data.get('Password')
            try:
                obj = User.objects.get(Name=name,Password = passwd)

            except User.DoesNotExist :
                return render(request,self.template_name,context={'form':form})
            return HttpResponseRedirect('/account/userdata/')

class UserDataView(views.View):
    template_name = 'account/user_data.html'

    def get(self,request,*args,**kwargs):
        userdata = User.objects.all()
        return render(request,self.template_name,context={'userdata':userdata})

class UserDeleteView(views.View):

    def get(self,request,*args,**kwargs):
        uid = kwargs.get('id')
        try:
            obj = User.objects.get(id = uid)
            obj.delete()
        except User.DoesNotExist :
            return HttpResponseRedirect('/account/userlogin')
        return HttpResponseRedirect('/account/userdata/')

class UserUpdateView(views.View):
    template_name = 'account/user_update.html'
    UserUpdateViewForm = UserUpdateForm
    def get(self,request,*args,**kwargs):
        uid = kwargs.get('id')

        try:
            obj = User.objects.get(id = uid)
            form = self.UserUpdateViewForm(instance=obj)
            return render(request,self.template_name,context={'form':form,'obj':obj})

        except User.DoesNotExist :
            form = self.UserUpdateViewForm()
            return render(request,self.template_name,context={'form':form})

    def post(self,request,*args,**kwargs):
        uid = kwargs.get('id')
        try:
            obj = User.objects.get(id = uid)
            form = self.UserUpdateViewForm(request.POST,instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/account/userdata/')
        except User.DoesNotExist :
            return render(request,self.template_name,context={'form':form})