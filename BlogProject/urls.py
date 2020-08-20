"""BlogProject URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from posts.views import index, blog, post, search, post_create, post_delete, post_update, confirm, delete, \
    register, loginPage, logoutUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path("blog/", blog, name='post-list'),
    path("search/", search, name='search'),
    path('tinymce/', include('tinymce.urls')),
    path('create/', post_create, name='post-create'),
    path("post/<int:pk>/", post, name='post-detail'),
    path('post/<int:pk>/delete/', post_delete, name='post-delete'),
    path('post/<int:pk>/update/', post_update, name='post-update'),
    path('confirm/', confirm, name='confirm'),
    path('delete/', delete, name='delete'),
    path('login/', loginPage, name="login"),
    path('register/', register, name="register"),
    path('logout/', logoutUser, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
