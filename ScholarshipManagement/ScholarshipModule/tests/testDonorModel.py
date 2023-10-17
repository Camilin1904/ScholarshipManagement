from django.test import TestCase
from ScholarshipModule.models import Donors


class ScholarshipModelTest(TestCase):

    def testCreateScholarship(self):
        don = Donors.objects.create(ID = 12345,
                                    name = "jijijija")
        self.assertEqual(don.name, "jijijija")
        self.assertEqual(don.ID, 12345)
