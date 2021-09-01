from django.contrib import admin

from .models import Resume, ResumeTemplate, JobExperience


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass


@admin.register(ResumeTemplate)
class ResumeTemplate(admin.ModelAdmin):
    pass


@admin.register(JobExperience)
class JobExperience(admin.ModelAdmin):
    pass
