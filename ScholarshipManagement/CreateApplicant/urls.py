from django.urls import path
from . import views
urlpatterns = [
    path('applicants/create/', views.createApplicants, name='Applicants'),
    path('applicants/', views.applicants, name='Applicants'),
    path('applicants/homePage/', views.homeApplicant, name='ApplicantsHomePage'),
]