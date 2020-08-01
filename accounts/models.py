from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver

# from accounts.managers import Department

class UserManager(BaseUserManager):
	def _create_user(self, name, email, password, regdno, department, **extras):
		user = self.create(
			name = name,
			email = self.normalize_email(email),
			regdno = regdno,
			department = Department.objects.get(id = department),
			**extras
			)
		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_user(self, name, email, password, regdno, department, **extras):
		extras.setdefault("is_staff", False)
		extras.setdefault("is_hod", False)
		extras.setdefault("is_active", False)
		extras.setdefault("is_admin", False)
		extras.setdefault("is_superuser", False)

		return self._create_user(name, email, password, regdno, department, **extras)

	def create_hod(self, name, email, password, regdno, department, **extras):
		extras.setdefault("is_staff", True)
		extras.setdefault("is_hod", True)
		extras.setdefault("is_active", False)
		extras.setdefault("is_admin", False)
		extras.setdefault("is_superuser", False)


		if extras.get('is_staff') is False:
			raise ValueError("HOD must have staff previliges.")
		return self._create_user(name, email, password, regdno, department, **extras)

	def create_admin(self, name, email, password, regdno, department, **extras):
		extras.setdefault("is_staff", True)
		extras.setdefault("is_hod", True)
		extras.setdefault("is_active", False)
		extras.setdefault("is_admin", True)
		extras.setdefault("is_superuser", False)


		if extras.get('is_staff') is False:
			raise ValueError("Admin must have staff previliges.")
		
		return self._create_user(name, email, password, regdno, department, **extras)

	def create_superuser(self, name, email, password, regdno, department, **extras):
		extras.setdefault("is_staff", True)
		extras.setdefault("is_hod", True)
		extras.setdefault("is_active", False)
		extras.setdefault("is_admin", True)
		extras.setdefault("is_superuser", True)


		if extras.get('is_staff') is False:
			raise ValueError("Super User must have all previliges.")
		
		return self._create_user(name, email, password, regdno, department, **extras)

class Department(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class User(AbstractUser, PermissionsMixin):
	name = models.CharField(_("name"), max_length=100)
	regdno = models.CharField(_("regd no"), max_length=30,unique = True)
	email = models.EmailField(_("email"))
	department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null = True)
	is_staff = models.BooleanField(default=False)
	is_hod = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	
	objects = UserManager()

	USERNAME_FIELD = 'regdno'
	REQUIRED_FIELDS = ['name', "email", "department"]
	

	def __str__(self):
		return self.name

@receiver(pre_save, sender = User)
def my_callback(sender, instance, *args, **kwargs):
    dept = Department.objects.get(instance.department)

    if dept is None:
    	Department.objects.create(instance.department)