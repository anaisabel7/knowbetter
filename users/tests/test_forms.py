from django.test import TestCase
from users.forms import MyUserCreationForm, MyUserChangeForm
from users.models import User

class MyUserCreationFormTestCase(TestCase):

    def test_meta_class(self):
        self.assertEqual(MyUserCreationForm().Meta.model, User)


class MyUserChangeFormTestCase(TestCase):

    def test_meta_class(self):
        self.assertEqual(MyUserChangeForm().Meta.model, User)