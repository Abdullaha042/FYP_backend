from django.test import TestCase

from .models import usersAuthentication
# Create your tests here.

class NewUserTestCase(TestCase):
    def setUp(self):
        usersAuthentication.objects.create(name='testingName1',username='testingUserName1',department='abcd1',password='123456781')
        usersAuthentication.objects.create(name='testingName2',username='testingUserName2',department='abcd2',password='123456782')


    def test_newuser_test(self):
        obj1 = usersAuthentication.objects.get(name='testingName1')
        obj2 = usersAuthentication.objects.get(name='testingName2')

        self.assertEqual(obj1.name,'testingName1')
        self.assertEqual(obj2.name,'testingName2')
