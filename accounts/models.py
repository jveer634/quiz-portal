from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from accounts.managers import UserManager

from sections.models import Department, Section

User = get_user_model()

class Staff(models.Model):
	user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
	is_hod = models.BooleanField(default=False)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	regdno = models.CharField(max_length=20, unique=True)

	class Meta:
		verbose_name_plural = "Staff"

	def __str__(self):
		return "{} {}".format(self.user.first_name, self.user.last_name)


class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	section = models.OneToOneField(Section, on_delete=models.CASCADE)

	def __str__(self):
		return "{} {}".format(self.user.first_name, self.user.last_name)