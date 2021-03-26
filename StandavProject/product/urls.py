from django.urls import include, path,re_path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from product.views import *

urlpatterns = [
	path('signup/',Usersignup.as_view()),
    path('login/',UserLogin.as_view()),
    path('logout/',UserLogOut.as_view()),
    path('product/',UserProduct.as_view()),
    path('add-product/',UserAddProduct.as_view()),
    ]
