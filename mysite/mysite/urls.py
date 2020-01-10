"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from core import views
from rest_framework import routers
# Code for the API
router = routers.DefaultRouter()
router.register('Books',views.BookView)
router.register('Posts',views.PostView)
router.register('Categories',views.TutiCateView)
router.register('TutorialSeries',views.TutorialSeriesView)

urlpatterns = [
    path('api/',include(router.urls)),
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('secret/', views.secret_page,name='secret'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('signup/',views.signup,name='signup'),
    path('upload/',views.upload,name='upload'),
    path('books/',views.book_list,name='book_list'),
    path('books/upload/',views.upload_book,name='upload_book'),
    path('create_post/',views.create_post,name="create_post",),
    path('posts/',views.post_list,name='post_list'),
    path('ask_question/',views.create_question,name='create_question'),
    path('aboutMI/',views.aboutMI, name="aboutMI"),    
    path('learn_more/',views.Learn_more, name="index"), 
    path('donate/',views.donate,name="donate"),
    path('learn_python/',views.homepage_learn,name="homepage_learn"),
    path('users/',views.user_list,name='user_list'),
    path('users_profile/',views. user_profile,name=' user_profile'),
    path('cv/',views.cv_upload,name='cvs'),
    path('web-development/',views.webDevelopment,name='webdevelopement'),
    path('edit/',views.edit_profile,name='edit-profilr')

  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)