"""nopal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from management.views import cambiarContra

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('administracion/', include('management.urls')),
    path('facturacion/', include('invoice.urls')),
    
    #  # Logueo
    path('admin-login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='admin-login'),
    path('admin-logout/', auth_views.LogoutView.as_view(), name='admin-logout'),
    
    #recuperacion
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='login/password-email.html',email_template_name='login/password_reset_email.html'),
         name='password-reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='login/new-password.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='login/account-recovery.html'), name='password_reset_complete'),
    path('reset/password_change/', auth_views.PasswordChangeView.as_view(template_name='login/login-wifi.html'),name='password_change'),
    path('cambioC', cambiarContra, name="password_change"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
