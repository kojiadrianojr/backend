"""
URL configuration for ApiRoot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from django.urls import path, include

from auth.views import LogoutView
from routers import router

urlpatterns = [
    path("admin/", admin.site.urls),

    # Register the auth endpoint--we use the djoser
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    # Create the logout
    path("auth/logout/", LogoutView.as_view()),

    # defines a path that includes all URLs from the router, prefixed with 'api/'
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/", include((router.urls, 'core_api'), namespace='core_api'))
    
]