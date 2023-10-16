from django.test import TestCase
from ScholarshipModule.models import User


class TestUser(TestCase):
    def testCreationUser(self):
        newUser= User.objects.create(
            username="andrescamiloromero22@gmail.com", name="Andrés Camilo Romero", role=0)
        self.assertEqual(newUser.username, "andrescamiloromero22@gmail.com")
        self.assertEqual(newUser.name, "Andrés Camilo Romero")
        self.assertEqual(newUser.role, 0)




