from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User

class MyUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields


class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields