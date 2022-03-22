from django.contrib import admin
from .models import University,Program, Proffessor, Scholarship, Country




@admin.register(Proffessor)
class ProffessorAdmin(admin.ModelAdmin):
    list_display = ['name','affiliation', 'email', 'researchgate', 'website', 'google_scholar']
    search_fields = ['name', 'affiliation']

class ProffessorInline(admin.StackedInline):
    model = Proffessor
    extra = 0


@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'deadline']
    search_fields = ['name']

    
class ScholarshipInline(admin.StackedInline):
    model = Scholarship
    extra = 0

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['subject', 'Deadline', 'link']
    search_fields = ['subject']
    list_filter = ['program_type', 'Deadline']
    inlines = [ProffessorInline]


class ProgramInline(admin.StackedInline):
    model = Program
    extra = 0

@admin.register(University)
class UniveristyAdmin(admin.ModelAdmin):
    list_display = ['name','location', 'ranking', 'website']
    search_fields = ['name',]
    list_filter = [ 'ranking']
    inlines = [ScholarshipInline, ProgramInline]

class UniversityIline(admin.StackedInline):
    model = University
    extra = 0

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    inlines = [UniversityIline,]
