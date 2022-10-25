from django.contrib import admin
from .models import Contact, CvURL, Profile, Education, Projects, Skills, Work,CvURL

admin.site.register(Profile)

admin.site.register(Work)

admin.site.register(Education)

admin.site.register(Projects)

admin.site.register(Skills)

admin.site.register(CvURL)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
