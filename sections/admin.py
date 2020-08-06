from django.contrib import admin

from sections.models import (
	Section, College, Department, SectionSubjectFaculty, Subject
	)


admin.site.register(Section)
admin.site.register(College)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(SectionSubjectFaculty)

