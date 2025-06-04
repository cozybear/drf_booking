"""
URL configuration for proj_booking project.

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
from django.urls import path, include
from app_booking.views import ClubAV, SlotAV, BookAV

urlpatterns = [

    # path('allsports/', all_sports, name='sportlist'),
    # path('allclubs/',all_clubs, name="clubslist"),
    # path('allavailable/', all_available, name="availableclubs"),
    path('listclubs/', ClubAV.as_view(), name="bookclub"),
    path('listslot/', SlotAV.as_view(), name='listslot'),
    path('bookslot/', BookAV.as_view(), name='bookslot'),
    
]
