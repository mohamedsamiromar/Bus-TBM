"""swvl_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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


from rest_framework.authtoken import views
from swvl.views import CaptinListApi, PassengerView, RegisterView, LoginAPI
from swvl.views import WhereFrom, CreateTrip, Reserved, TakeTrip, BusView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('where_from', WhereFrom.as_view()),
    path('create_trip', CreateTrip.as_view(), name='trip'),
    path('reserved_view/<int:pk>', Reserved.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('take_trip', TakeTrip.as_view()),
    # token_url
    path('token-auth', views.obtain_auth_token, name='api_token_auth'),
    # generic
    path('captin', CaptinListApi.as_view(), name="create_captin"),
    path('passeger', PassengerView.as_view(), name="Create_passenger"),
    path('bus', BusView.as_view(), name="bus"),
    # Register
    path('register', RegisterView.as_view(), name='register'),
    # Login
    path('login', LoginAPI.as_view(), name='login')
]
