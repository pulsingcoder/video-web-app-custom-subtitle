"""
URL configuration for video_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from studio import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from studio.views import SignUpView


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('studio/', views.studio, name='studio'),
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),
    path(
        "login/",
        LoginView.as_view(
            # name of the login template
            template_name="studio/login.html",
            # user will be redirected to index page upon successful login
            next_page="/studio",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),

    path(
        "logout/",
        LogoutView.as_view(next_page="/login"),
        name="logout",
    ),
    # Added signup view here
    path("signup/", SignUpView.as_view(), name="signup"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
