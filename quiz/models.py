from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify


User = get_user_model()

class Subject(models.Model):
	name = models.CharField("Subject Name", max_length=100)

	def __str__(self):
		return self.name

class Quiz(models.Model):
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	description = models.TextField()
	slug = models.SlugField()
	marks = models.IntegerField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	start = models.DateTimeField(auto_now_add=False, auto_now=False)
	end = models.DateTimeField(auto_now_add=False,auto_now=False)

	class Meta:
		verbose_name_plural = "Quizzes"


	def __str__(self):
		return self.name

class Question(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	label = models.CharField("Question",max_length=120)

	def __str__(self):
		return self.label

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	label = models.CharField("Option",max_length=150)
	correct = models.BooleanField(default=False)


	@property
	def is_correct(self):
		return self.is_correct	

	def __str__(self):
		return self.label

class QuizTaker(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	score = models.IntegerField(default=None)
	completed = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now=True)
	submitted_on = models.DateTimeField(auto_now=False, auto_now_add=False)

	class Meta:
		verbose_name_plural = "Quiz Takers"

	
	@property
	def is_completed(self):
		return self.is_completed

	def __str__(self):
		return self.user.username

class UsersAnswer(models.Model):
	quiztaker = models.ForeignKey(QuizTaker, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

	
@receiver(pre_save, sender=Quiz)
def slugify_name(self, instance, *args, **kwargs):
	instance.slug = slugify(instance.name)