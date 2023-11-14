from django.test import TestCase
from ScholarshipModule.models import Applicant


class TestApplicant(TestCase):

    def testCreationApplicant(self):
        applicant = Applicant.objects.create(
            name = "Juan Carlos", lastName = "Rios Garcia", ID = 12,
            studentCode = "A00302613", faculty = "Ingenieria", major = "Sistemas",
            semester = 2, email = "juanCar22@gmail.com", phone = 322717233,
            status = 1)
        self.assertEqual(applicant.name, "Juan Carlos")
        self.assertEqual(applicant.lastName, "Rios Garcia")
        self.assertEqual(applicant.ID, 12)
        self.assertEqual(applicant.studentCode, "A00302613")
        self.assertEqual(applicant.faculty, "Ingenieria")
        self.assertEqual(applicant.major, "Sistemas")
        self.assertEqual(applicant.semester, 2)
        self.assertEqual(applicant.email, "juanCar22@gmail.com")
        self.assertEqual(applicant.phone, 322717233)
        self.assertEqual(applicant.status, 1)

