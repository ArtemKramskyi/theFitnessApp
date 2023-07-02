from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ExercisesCatalog, Program, Plan

admin.site.site_header = "The Fitness App Admin"
admin.site.index_title = "Welcome to the fitness app admin area"
admin.site.site_title = "My App"


class ExercisesCatalogAdmin(admin.ModelAdmin):
    list_display = ('exerciseName', 'category', 'sets', 'reps')


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('programName', 'user')


admin.site.register(User, UserAdmin),
admin.site.register(ExercisesCatalog, ExercisesCatalogAdmin),
admin.site.register(Program, ProgramAdmin),
admin.site.register(Plan)
