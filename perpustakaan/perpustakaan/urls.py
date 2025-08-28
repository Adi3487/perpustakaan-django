from django.contrib.auth import views as auth_views 
from django.contrib import admin
from django.urls import path,include
from user import views as user_views
from perpustakaan.views import home 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', home, name='home'), 
    path("accounts/login/",auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", user_views.signup, name= "signup"),
    path("",include("buku.urls")), #pake ini biar lebih spesifik 

    
    
    
    
    
    
    
    
    
    
    
    
    
    ]
