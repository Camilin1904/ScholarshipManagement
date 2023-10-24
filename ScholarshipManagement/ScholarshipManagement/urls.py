"""
URL configuration for ScholarshipManagement project.

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
from django.urls import path, include
from ScholarshipModule import views
from ScholarshipModule import createApplicant
from ScholarshipModule import filterApplicant


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signUp, name = 'signup'),
    path('home/', views.home, name = 'home'),
    path('scholarships/', views.scholarships, name='scholarships'),
    path('announcement/create/', views.createAnnouncement, name='createAnnouncement'),
    path('scholarships/create/', views.createScholarships, name = 'createScholarships'),
    path('logout/', views.signOut, name = 'signOut'),
    path('login/', views.signIn, name = 'signIn'),
    path('roles/', views.searchUserForRole, name = 'searchUser'),
    path('roles/', views.searchUserForRole, name = 'roleAssign'),
    path('announcement/', views.searchAnnouncement, name = 'announcement'),
    path('applicants/edit', views.editApplicant, name = 'editApplicant'),
    path('searchStudent/', filterApplicant.filterApplicants, name = 'searchStudent'),
    path('applicants/create/', createApplicant.createApplicants, name='Applicants'),
    path('view/Student/', views.viewApplicant, name = 'viewStudent')
]   


