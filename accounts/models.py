from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from accounts.managers import UserManager

from sections.models import Department, Section


class User(AbstractUser, PermissionsMixin):
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	name = models.CharField(_("name"), max_length=100)
	regdno = models.CharField(_("regd no"), max_length=30,unique = True)
	email = models.EmailField(_("email"))
	is_staff = models.BooleanField(default=False)
	is_hod = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	
	objects = UserManager()

	USERNAME_FIELD = 'regdno'
	REQUIRED_FIELDS = ['name', "email"]
	

	def __str__(self):
		return self.name

class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	section = models.OneToOneField(Section, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.name