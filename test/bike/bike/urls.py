"""
URL configuration for bike project.

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
from django.urls import path
from mybike import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("bike/add/",views.BikeCreateView.as_view(),name="bike-add"),
    
    path("bike/all/",views.BikeListView.as_view(),name="bike-list"),
    
    path("bike/<int:pk>/remove/",views.BikeDeleteView.as_view(),name="bike-delete"),
    
    path("bike/<int:pk>",views.BikeDetailView.as_view(),name="bike-detail"),
    
    path("bike/<int:pk>/update/",views.BikeUpdateView.as_view(),name="bike-update"),
    
    
    
]  +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

