from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """This is for User Profile Manager"""
    
    
    def create_user(self, email, name, password=None):
        """This is for creating user"""
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_superuser(self, email, name, password):
        """This is for creating super user"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_Admin = True
        user.save(using=self.db)

        return user
    

class UserProfile(AbstractBaseUser, PermissionMixin):
    """This is for the User Profile """
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_Admin = models.BooleanField(default=False)
    id_Active = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FILED = 'email'
    REQUIRED_FILED = ['name']

    def get_full_name(self):
        """This is for getting full name"""
        return self.name
    def get_short_name(self):
        """This is for getting short name"""
        return self.name
    def __str__(self):
        """This is for returning string"""
        return self.email



    
