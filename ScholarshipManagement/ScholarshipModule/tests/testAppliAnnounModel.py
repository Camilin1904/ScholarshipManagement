from django.test import TestCase
from ScholarshipModule.models import AnnouncementAndApplicant
from ScholarshipModule.models import Applicant
from ScholarshipModule.models import Announcements



class TestApplicant(TestCase):

    def testCreationApplicant(self):
        announcementTest = Announcements.objects.create(id = 6, type = 0)
        applicantTest = Applicant.objects.create(
            name = "Juan Carlos", lastName = "Rios Garcia", ID = 29,
            studentCode = "A00302613", faculty = "Ingenieria", major = "Sistemas",
            semester = 2, email = "juanCar22@gmail.com", phone = 322717233)
        relation = AnnouncementAndApplicant.objects.create(
            ID = 29, announcement = announcementTest , applicant = applicantTest)
        self.assertEqual(relation.ID, 29)
        self.assertEqual(relation.announcement.id, 6)
        self.assertEqual(relation.applicant.ID, 29)


