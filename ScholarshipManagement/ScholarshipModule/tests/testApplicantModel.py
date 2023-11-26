from django.test import TestCase
from ScholarshipModule.models import Applicant


class TestApplicant(TestCase):

    def testCreationApplicant(self):
        applicant = Applicant.objects.create(
            name = "Juan Fernando", lastName = "Rios Garcia", ID = 29,
            studentCode = "A00380637", faculty = "Ingeniería, Diseño y Ciencias Aplicadas", major = "Ingeniería de Sistemas",
            semester = 2, email = "juanCar21@gmail.com", phone = 322717233,
            status = 1)
        self.assertEqual(applicant.name, "Juan Fernando")
        self.assertEqual(applicant.lastName, "Rios Garcia")
        self.assertEqual(applicant.ID, 29)
        self.assertEqual(applicant.studentCode, "A00380637")
        self.assertEqual(applicant.faculty, "Ingeniería, Diseño y Ciencias Aplicadas")
        self.assertEqual(applicant.major, "Ingeniería de Sistemas")
        self.assertEqual(applicant.semester, 2)
        self.assertEqual(applicant.email, "juanCar21@gmail.com")
        self.assertEqual(applicant.phone, 322717233)
        self.assertEqual(applicant.status, 1)

