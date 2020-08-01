from django.contrib import admin
from accounts.models import User
from accounts.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
	add_form = UserCreationForm
	form = UserChangeForm
	model = User
	list_display = ('regdno', 'name', 'email', 'department')
	list_filter = ('regdno', 'name', 'email', 'department')
	fieldsets = (
		(None, {'fields': ('name', 'regdno', 'email', 'department')}),
		('Permissions', {'fields' : ('is_staff', 'is_hod', 'is_admin', 'is_superuser')})
	)
	search_fields = ('regdno', 'name')
	ordering = ('department', 'regdno')

admin.site.register(User, UserAdmin)