from django.test import TestCase
from .models import Announcements


class AnnouncementTest(TestCase):
    def testCreationAnnouncement(self):
        newAnnouncement= Announcements.objects.create(studentId=1, scholarshipId=2)
        self.assertEqual(newAnnouncement.studentId,1)
        self.assertEqual(newAnnouncement.scholarshipId,2)




