from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    UserManager class for handling custom user model.
    Creation of super user and non super user
    """

    def create_user(self, email, password=None, **extra_fields):
        """ Creates and saves a new user """
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        """ Create a new super user """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user
