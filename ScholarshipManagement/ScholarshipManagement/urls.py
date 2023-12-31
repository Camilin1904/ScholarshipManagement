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
from ScholarshipModule.views import filterOfReport
from ScholarshipModule.views import login
from ScholarshipModule.views import logout
from ScholarshipModule.views import objectOfReport
from ScholarshipModule.views import reportResume
from ScholarshipModule.views import searchUserForRole
from ScholarshipModule.views import signUp
from ScholarshipModule.views import createScholarship
from ScholarshipModule.views import typeOfReport
from ScholarshipModule.views import scholarshipView
from ScholarshipModule.views import scholarshipEdit
from ScholarshipModule.views import createScholarship
from ScholarshipModule.views import scholarships
from ScholarshipModule.views import deleteScholarship
from ScholarshipModule.views import pdf
from ScholarshipModule.views import images
from ScholarshipModule.views import createApplicant
from ScholarshipModule.views import filterApplicant
from ScholarshipModule.views import createAppliStep3
from ScholarshipModule.views import editApplicant
from ScholarshipModule.views import viewApplicant
from ScholarshipModule.views import stateCheckFilter
from django.conf import settings
from django.conf.urls.static import static
from ScholarshipModule.views import createScholarship
from ScholarshipModule.views import createAnnouncement
from ScholarshipModule.views import searchAnnouncement
from ScholarshipModule.views import viewAnnouncement
from ScholarshipModule.views import editAnnouncement
from ScholarshipModule.views import home
from ScholarshipModule.views import viewCalendar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signUp.signUp, name = 'signup'),
    path('home/', home.home, name = 'home'),
    path('scholarships/', scholarships.scholarships, name='scholarships'),
    path('announcement/create/', createAnnouncement.createAnnouncement, name='createAnnouncement'),
    #path('scholarships/create/', views.createScholarships, name = 'createScholarships'),
    path('applicants/edit', editApplicant.editApplicant, name = 'editApplicant'),
    path('searchStateCheck/', stateCheckFilter.stateCheckFilter, name='searchStateCheck'),
    path('view/Student/', viewApplicant.viewApplicant, name = 'viewStudent'),
    path('searchStudent/', filterApplicant.filterApplicants, name = 'searchStudent'),
    path('applicants/create/', createApplicant.createApplicants, name='Applicants'),
    path('applicants/create/step3/', createAppliStep3.createAppliStep3, name='ApplicantStep2'),
    #path('scholarships/create/', views.createScholarships, name = 'createScholarships'),
    path('logout/', logout.signOut, name = 'signOut'),
    path('login/', login.signIn, name = 'signIn'),
    path('roles/', searchUserForRole.searchUserForRole, name = 'searchUser'),
    path('roles/', searchUserForRole.searchUserForRole, name = 'roleAssign'),
    path('announcement/', searchAnnouncement.searchAnnouncement, name = 'announcement'),   
    path('objectOfReport/', objectOfReport.objectOfReport, name = 'reportGenerator'),
    path('typeOfReport/', typeOfReport.typeOfReport, name = 'reportGenerator'),
    path('filterOfReport/', filterOfReport.filterOfReport, name = 'reportGenerator'),
    path('reportResume/', reportResume.reportResume, name = 'reportPreview'),
    path('scholarships/create/', createScholarship.createScholarshipsSC1, name = 'createScholarships'),
    path('pdf/', pdf.render_pdf_view, name = 'pdf'),
    path('announcement/edit/', editAnnouncement.editAnnouncement, name = 'editAnnouncement'),
    path('announcement/view/', viewAnnouncement.viewAnnouncement, name = 'viewAnnouncement'),
    path('createEvent/', editAnnouncement.createEvent, name = 'createEvent'),
    path('announcement/edit/events/', editAnnouncement.editEvent, name = 'editEvent'),
    path('announcement/calendar/', viewCalendar.viewCalendar, name = 'calendar'),
    path('scholarships/edit/',scholarshipEdit.scholarshipEdit,name ='editScholarship'),
    path('scholarships/view/',scholarshipView.scholarshipView,name='viewScholarship'),
    path('scholarships/delete/', deleteScholarship.deleteScholarship, name='delScholarship')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



