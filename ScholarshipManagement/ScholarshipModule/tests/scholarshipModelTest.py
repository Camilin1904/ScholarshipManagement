from django.test import TestCase
from ScholarshipModule.models import Scholarships
from ScholarshipModule.models import Donors


class ScholarshipModelTest(TestCase):

    def testCreateScholarship(self):
        don = Donors.objects.create(ID = 12345,
                                    name = "jijijija")
        sch = Scholarships.objects.create(name="test", 
            ID=123, description="test test",
            donor=don, coverage=12345, 
            type=2, requirements="none")
        self.assertEqual(sch.name, "test")
        self.assertEqual(sch.ID, 123)
        self.assertEqual(sch.description, "test test")
        self.assertEqual(sch.donor.ID, don.ID)
        self.assertEqual(sch.coverage, 12345)
        self.assertEqual(sch.type, 2)
        self.assertEqual(sch.requirements, "none")
