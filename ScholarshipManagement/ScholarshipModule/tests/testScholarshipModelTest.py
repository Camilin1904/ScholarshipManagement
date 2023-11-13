from django.test import TestCase
from ScholarshipModule.models import Scholarships
from ScholarshipModule.models import Donors
from ScholarshipModule.models import ScholarsipTypes


class ScholarshipModelTest(TestCase):

    def testCreateScholarship(self):
        don = Donors.objects.create(ID = 12345,
                                    name = "jijijija")
        sch = Scholarships.objects.create(name="test", 
            ID=123, description="test test",
            donor=don, requirements="none")
        
        types = ScholarsipTypes.objects.create(
            scholarship=Scholarships.objects.get(ID=sch.ID), 
            unit=0, 
            value=100, 
            type="Alimentación")
        
        self.assertEqual(sch.name, "test")
        self.assertEqual(sch.ID, 123)
        self.assertEqual(sch.description, "test test")
        self.assertEqual(sch.donor.ID, don.ID)
        self.assertEqual(sch.requirements, "none")
        self.assertEqual(types.scholarship.ID, 123)
        self.assertEqual(types.unit, 0)
        self.assertEqual(types.value, 100)
        self.assertEqual(types.type, "Alimentación")
