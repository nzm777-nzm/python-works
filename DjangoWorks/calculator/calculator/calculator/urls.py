"""
URL configuration for calculator project.

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
from operations.views import AdditionView,SubtactionView,MultiplicationView
from operations.views import DivisionView
from operations.views import CubeView
from operations.views import FactorialView
from operations.views import BmiView
from operations.views import BmrView,EmiView,GainorlossView,MilageView,PercentageView,ConversionView,LeapyearView,SignupView,CustomerView,IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',AdditionView.as_view(),name="addition"),
    path('sub/',SubtactionView.as_view(),name="subraction"),
    path('multi/',MultiplicationView.as_view(),name="multiplication"),
    path('div/',DivisionView.as_view(),name="division"),
    path('cube/',CubeView.as_view(),name="cube"),
    path('fact/',FactorialView.as_view(),name="factorial"),
    path('bmi/',BmiView.as_view(),name="BMI"),
    path('bmr/',BmrView.as_view(),name="BMR"),
    path('emi/',EmiView.as_view(),name="emi"),
    path('gain/',GainorlossView.as_view(),name="weightgain"),
    path('mile/',MilageView.as_view(),name="milage"),
    path('perc/',PercentageView.as_view(),name="percentage"),
    path('temp/',ConversionView.as_view(),name="conversion"),
    path('year/',LeapyearView.as_view(),name="years"),
    path('sign/',SignupView.as_view(),name="signup"),
    path('cust/',CustomerView.as_view(),name="customer"),
    path("",IndexView.as_view())
]
