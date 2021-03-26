from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from product.models import *
from django.views.generic import View
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserLogin(View):

    def get(self, request):
        return render(request,'user_login.html',locals())

    @csrf_exempt
    def post(self,request):
        self.user_name = request.POST.get('username', None)
        self.password = request.POST.get('password', None)

        self.user_authenticate()
        
        if self.user and self.user.is_active:
            login(request, self.user)
            return redirect('/product/')
        else:
            error_msg = "Your User ID & Password Combination is Incorrect" 
        return render(request,'user_login.html',locals())

    def user_authenticate(self):

        try:
            username = User.objects.get(username=self.user_name.lower()).username
        except Exception as e:
            username = None
            self.password = None

        self.user = authenticate(username=username, password=self.password)


class UserProduct(View):

    def get(self, request):
        self.title = 'List of Products'
        if not request.user.is_authenticated:
            return redirect('/login/')
        user_name = User.objects.get(id=request.user.id)
        
        self.product_li = UserProductList.objects.filter(user_id = user_name).values()
        return render(request,'product_list.html',locals())

class UserAddProduct(View):
    def get(self, request):
        self.title = 'List of Products'
        if not request.user.is_authenticated:
            return redirect('/login/')
        return render(request,'new_user_product.html',locals())        

    def post(self, request):
        self.title = 'List of Products'
        if not request.user.is_authenticated:
            return redirect('/login/')

        self.post_data = request.POST
        user_name = User.objects.get(id=request.user.id)
       
        self.product_li = UserProductList.objects.create(user_id = user_name, product_name =self.post_data['product_name'])
        return redirect('/product/')


class Usersignup(View):
    
    def get(self, request):
        form = UserCreationForm()
        return render(request,'new_user_sign_up.html',locals())        

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')


class UserLogOut(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')