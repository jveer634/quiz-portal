from django.db import models


YEAR_CHOICES = (
		(1, "1st Year"),
		(2, "2nd Year"),
		(3, "3rd Year"),
		(4, "4th Year")
	)

class Department(models.Model):
	name = models.CharField("Department name", max_length=120)

	def __str__(self):
		return self.name


class Section(models.Model):
	name = models.CharField("Section Name", max_length=25)
	year = models.IntegerField(choices=YEAR_CHOICES)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Subject(models.Model):
	name = models.CharField("Name", max_length=120)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
from django.contrib.auth import get_user_model

User = get_user_model()


class SectionSubjectFaculty(models.Model):
	section = models.ForeignKey(Section, on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	faculty = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return "{} {} {}".format(self.section, self.subject, self.faculty)
