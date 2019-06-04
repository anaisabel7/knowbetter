from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.forms import MyUserCreationForm, MyUserChangeForm
from users.models import User

class MyUserAdmin(UserAdmin):

    creation_form = MyUserCreationForm
    form = MyUserChangeForm
    model = User

admin.site.register(User, MyUserAdmin)
