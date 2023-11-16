from django.test import TestCase
from ScholarshipModule.models import *

class AccessToCreationApplicantTest(TestCase):

    def setup(cls):

        testUser1 = User.objects.create(username = 'prueba@gmail.com',name='Prueba',password = 'siasies',role='1')
        testUser2 = User.objects.create(username = 'prueba2@gmail.com',name='Prueba2',password = 'siasies2',role='3')

        testUser1.save()
        testUser2.save()

    def testRedirectIfNotLoggedIn(self):

        response = self.client.get('/applicants/create/')
        self.assertEqual(response.status_code,302)
    
