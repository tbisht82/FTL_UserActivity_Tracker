import random
import string
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from timezone_field import TimeZoneField
from .manager import UserManager


def id_generate():
    """
    Generate a new user_id while creating user
    :return: alphanumeric user_id
    """

    letters_and_digits = string.ascii_uppercase + string.digits
    id_new = ''.join(random.choice(letters_and_digits) for i in range(7))
    id_new = 'W0'+id_new
    if id_already_exist(id_new):
        return id_new
    else:
        id_generate()


def id_already_exist(id_new):
    """
    Checks whether newly generated id by id_generate() already exist in db or it is a unique user_id
    :param id_new:
    :return: boolean
    """

    q = User.objects.filter(user_id=id_new).count()
    if q == 0:
        return True
    else:
        return False


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model that supports email in place of username """
    user_id = models.CharField(primary_key=True, max_length=20, default=id_generate, editable=False)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    timezone = TimeZoneField(default='America/Los_Angeles')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class ActivityPeriod(models.Model):
    """
    ActivityPeriod model contains start and end time for user's activity.
    """
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def __self__(self):
        return str(self.start_time) + str(self.user)
