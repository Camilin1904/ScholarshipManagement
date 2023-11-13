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
from ScholarshipModule.views2 import createApplicant
from ScholarshipModule.views2 import filterApplicant
from ScholarshipModule.views2 import createAppliStep3
from django.conf import settings
from django.conf.urls.static import static
from ScholarshipModule import reportsViews
from ScholarshipModule.views2 import CreateScholarship
from ScholarshipModule.views2 import Scholarships
from ScholarshipModule.views2 import createAnnouncement
from ScholarshipModule.views2 import searchAnnouncement
from ScholarshipModule.views2 import viewAnnouncement
from ScholarshipModule.views2 import editAnnouncement


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signUp, name = 'signup'),
    path('home/', views.home, name = 'home'),
    path('scholarships/', Scholarships.scholarships, name='scholarships'),
    path('announcement/create/', createAnnouncement.createAnnouncement, name='createAnnouncement'),
    #path('scholarships/create/', views.createScholarships, name = 'createScholarships'),
    path('logout/', views.signOut, name = 'signOut'),
    path('login/', views.signIn, name = 'signIn'),
    path('roles/', views.searchUserForRole, name = 'searchUser'),
    path('roles/', views.searchUserForRole, name = 'roleAssign'),
    path('announcement/', searchAnnouncement.searchAnnouncement, name = 'announcement'),
    path('applicants/edit', views.editApplicant, name = 'editApplicant'),
    path('searchStudent/', filterApplicant.filterApplicants, name = 'searchStudent'),
    path('applicants/create/', createApplicant.createApplicants, name='Applicants'),
    path('applicants/create/step3/', createAppliStep3.createAppliStep3, name='ApplicantStep2'),
    path('view/Student/', views.viewApplicant, name = 'viewStudent'),
    path('objectOfReport/', reportsViews.objectOfReport, name = 'reportGenerator'),
    path('typeOfReport/', reportsViews.typeOfReport, name = 'reportGenerator'),
    path('filterOfReport/', reportsViews.filterOfReport, name = 'reportGenerator'),
    path('reportResume/', reportsViews.reportResume, name = 'reportPreview'),
    #path('example/', views.reportGenerator, name = 'reportGenerator'),
    path('scholarships/create/', CreateScholarship.createScholarshipsSC1, name = 'createScholarships'),
    path('announcement/edit/', editAnnouncement.editAnnouncement, name = 'editAnnouncement'),
    path('announcement/view/', viewAnnouncement.viewAnnouncement, name = 'viewAnnouncement'),
    path('createEvent/', editAnnouncement.createEvent, name = 'createEvent'),
    path('announcement/edit/events/', editAnnouncement.editEvent, name = 'editEvent'),
    path('announcement/calendar/', views.viewCalendar, name = 'calendar')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




