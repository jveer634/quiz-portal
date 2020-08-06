from django.contrib import admin
from accounts.models import Staff, Student
from django.contrib.auth import get_user_model

User = get_user_model()


admin.site.register(Staff)
admin.site.register(Student)

