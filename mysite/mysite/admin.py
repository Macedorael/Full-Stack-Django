from django.contrib import admin
from polls.models import Question, Choice

class CustomAdminSite(admin.AdminSite):
    site_header = 'Curso de Python Admin'

admin_site = CustomAdminSite()
admin_site.register(Question)
admin_site.register(Choice)

