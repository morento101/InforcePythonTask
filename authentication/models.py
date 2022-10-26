from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """Custom user manager which is responsible for creating users."""

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class Employee(AbstractUser):
    """Employee model."""

    class PositionChoices(models.IntegerChoices):
        """This class is used for choosing a position."""

        BACKEND = 0, "BackEnd Developer"
        FRONTEND = 1, "FrontEnd Developer"
        MOBILE = 2, "Mobile Developer"
        DEVOPS = 3, "DevOps"
        QA = 4, "QA"

    username = None
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=True)
    position = models.IntegerField(
        choices=PositionChoices.choices, default=PositionChoices.BACKEND
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def is_staff(self):
        """Determines whether user is admin."""
        return self.is_admin
