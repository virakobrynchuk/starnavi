from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views as local_view
from rest_framework.authtoken import views as rest_framework_views


urlpatterns = [
    path('entry/', local_view.get_auth_token, name='login'),
    path('signup/', local_view.signup, name='SignUp'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout2.html'), name='LogOut'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='LogIn'),
    path('token/', rest_framework_views.obtain_auth_token, name='get_auth_token'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


