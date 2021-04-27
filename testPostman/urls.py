"""testPostman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app01 import views as vs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app01/index/', vs.index),

    path('app01/login/', vs.login),
    path('app01/home/', vs.home),
    path('app01/logout/', vs.logout),

    path('app01/addUser/', vs.addUser),
    path('app01/showUser/', vs.showUser),

    path('app01/deleteUser/<int:id>', vs.deleteUser),

    path('app01/preUpdateUserById/<int:id>', vs.preUpdateUserById),
    path('app01/updateUser/', vs.updateUser),

]

