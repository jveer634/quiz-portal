from django.contrib import admin
from django.urls import path, include
from .views import index_view

urlpatterns = [
    path('', index_view),
    path("quiz", include('quiz.urls')),
	path('nested_admin', include('nested_admin.urls')),
    path('admin/', admin.site.urls),
]
