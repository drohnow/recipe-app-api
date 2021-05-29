from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionMixin

class BaseUserManager(BaseUserManager);
    def create_user, emal, password=None, **extra_fields):
        """creates and saves a new user"""

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionMixin):
    """customer user model"""
    email = models.EmailField(max_length=255, unique=True)
    name = mdoels.CharField(max_length=255)
    is_active = models.Booleanfield(default=True)
    is_staff = models.Booleanfield(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
