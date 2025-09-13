""" 
URL configuration for wscubetech project. 
The `urlpatterns` list routes URLs to views. For more information please see: 
https://docs.djangoproject.com/en/5.2/topics/http/urls/ 
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
from django.urls import path 
from wscubetech import views 
from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path("about-us/", views.about, name="about-us"),
    path("contact/", views.contact, name="contact"),
    path('', views.index, name='index'),  # Show index.html at root URL 
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
