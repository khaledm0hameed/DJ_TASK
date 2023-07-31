"""
URL configuration for project project.

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
from forum.views import Question_list,Question_detail,Question_delet , Question_create , Question_edit
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Question_list.as_view()),
    path('<int:pk>',Question_detail),
    path('<int:pk>/delet',Question_delet.as_view()),
    path('<int:pk>/new',Question_create.as_view()),
    path('<int:pk>/edit',Question_edit.as_view()),
]
