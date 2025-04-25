"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view( template_name='landing.html'),name='home'),
    path('login/', TemplateView.as_view( template_name='login.html'),name='login'),
    path('login/register.html', TemplateView.as_view( template_name='register.html'),name='login'),
    path('register/', TemplateView.as_view( template_name='register.html'),name='register'),
    path('register/login.html', TemplateView.as_view( template_name='login.html'),name='register'),
    path('register/login.html', TemplateView.as_view( template_name='register.html'),name='login'),
    path('landing/', TemplateView.as_view( template_name='landing.html'),name='landing'),
    path('login/login.html', TemplateView.as_view( template_name='login.html'),name='register'),
    path('landing/browse.html', TemplateView.as_view( template_name='browse.html'),name='landing'),
    path('login/landing.html', TemplateView.as_view( template_name='landing.html'),name='login'),
    path('register/landing.html', TemplateView.as_view( template_name='landing.html'),name='register'),
    path('login/browse.html', TemplateView.as_view( template_name='browse.html'),name='login'),
    path("register/",TemplateView.as_view(template_name="register.html"),name="register"),
    path('datasetDetails/', TemplateView.as_view( template_name='datasetDetails.html'),name='datasetDetails'),
    path('browse/datasetDetails.html', TemplateView.as_view( template_name='datasetDetails.html'),name='datasetDetails'),
    path("", include("datasetmanager.urls"), name="datasetmanager"),
    path("", include("authentication.urls"), name="auth"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)