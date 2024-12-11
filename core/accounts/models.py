from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.utils.translation import gettext_lazy as _

# Create a user manager class
class UserManager(BaseUserManager):
    """ 
    This is a Custom User Manager for our application.
    In this class, email must be unique indentifiers
    for authentication instead of username.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create & save a User with given email and password.
        """
        if not email:
            raise ValueError(_("The email must be set."))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create & save a Superuser with given email and password.
        """
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_staff") != True:
            raise ValueError(_("Superuser must be staff!(is_staff=True)"))
        if extra_fields.get("is_superuser") != True:
            raise ValueError(_("Superuser must be Superuser!(is_superuser=True)"))
        return self.create_user(email, password, **extra_fields)
        

# Create a custom user class
class User(AbstractBaseUser, PermissionsMixin):
    """
    A Custom User Model that we set some custom fields
    to it. In this model, email should be unique and
    set permission fields(like 'is_staff') to false.
    """
    email = models.EmailField(max_length=254, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    