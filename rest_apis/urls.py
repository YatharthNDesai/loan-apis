"""rest_apis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

import loan_apps.views
import loan_apps.api_views


urlpatterns = [
    path('apps/', include('loan_apps.urls')),
    path('admin/', admin.site.urls),
    path('api/status/<int:id>', loan_apps.api_views.LoanApplicationListById.as_view()),
    path('api/loanapps', loan_apps.api_views.LoanApplicationList.as_view()),
    path('api/loanapp', loan_apps.api_views.LoanApplicationCreate.as_view()),
    path('api/address', loan_apps.api_views.AddressList.as_view()),
    path('api/address/new', loan_apps.api_views.AddressCreate.as_view()),
    path('api/business', loan_apps.api_views.BusinessList.as_view()),
    path('api/business/new', loan_apps.api_views.BusinessCreate.as_view())
]
