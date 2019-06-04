from django.test import TestCase
from users.models import User

class UserTestCase(TestCase):

    def test__str__(self):
        user = User.objects.create(username='elvis')
        self.assertEqual(user.username, user.__str__())
# Create your tests here.
