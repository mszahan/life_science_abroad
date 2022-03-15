from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django_countries.fields import CountryField



class University(models.Model):
    name = models.CharField(max_length=150)
    ranking = models.IntegerField(blank=True, null=True)
    country = CountryField()
    location = models.CharField(max_length=250, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True)
    info = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.name



class Scholarship(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='scholarships')
    name = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    info = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.name


PROGRAM_CHOICES = (
    ('MSc', 'MSc'),
    ('PhD', 'PhD'),
)

class Program(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='programs')
    program_type = models.CharField(max_length=10, choices=PROGRAM_CHOICES)
    subject = models.CharField(max_length=250)
    Deadline = models.DateField(auto_now=False, auto_now_add=False)
    link = models.URLField(blank=True, null=True)
    info = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return f"{self.subject}-{self.university.name}"


class Proffessor(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='proffs')
    name = models.CharField(max_length=50)
    affiliation = models.TextField()
    email = models.EmailField(max_length=254, blank=True)
    contact = models.CharField(max_length=250, blank=True)
    website = models.URLField(blank=True, help_text='please use https://')
    researchgate = models.URLField(blank=True, help_text='please use https://')
    Orchid = models.URLField(blank=True, help_text='please use https://')
    google_scholar = models.URLField(blank=True, help_text='please use https://')

    def __str__(self):
        return self.name