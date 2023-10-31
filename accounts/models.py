from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from companies.models import Company

class UserManager(BaseUserManager):
    # Create standard user
    def create_user(self, email, full_name, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('O usuário deve informar um email')
        if not full_name:
            raise ValueError('O usuário deve informar o nome completo')
        if not password:
            raise ValueError('O usuário deve informar uma senha')
        user_obj = self.model(
            email = self.normalize_email(email),
            full_name = full_name
        )
        user_obj.set_password(password) # Defined user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.set_password(password) # Defined user password
        user_obj.save(using=self._db) # Defined user password
        return user_obj

    # Create a staff user
    def create_staff_user(self, email, full_name, password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff=True
        )
        return user

    # Create superuser
    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    seller = models.BooleanField(default=True)
    manager = models.BooleanField(default=False)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self): # Return the name of the user
        return self.full_name

    def get_first_name(self): # Return the firstname of the user
        first_name = self.full_name.split(' ')
        return first_name

    # def get_short_name(self):
    #     return self.email

    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

    # Check if is staff
    @property
    def is_staff(self):
        return self.staff

    # Check if is admin
    @property
    def is_admin(self):
        return self.admin

    # Check if is active
    @property
    def is_active(self):
        return self.active

    # Check if is seller
    @property
    def is_seller(self):
        return self.seller

    # Check if is manager
    @property
    def is_manager(self):
        return self.manager

