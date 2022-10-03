from django.db import models


class Profile(models.Model):
    age = models.PositiveBigIntegerField()
    Email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    langauge = models.CharField(max_length=50)
    about = models.CharField(max_length=500)


class Work(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    From = models.DateField()
    to = models.DateField()
    description = models.CharField(max_length=250)


class Education(models.Model):
    title = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


class Projects(models.Model):
    techstack = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    codelink = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


class Skills(models.Model):
    frameworks = models.CharField(max_length=100)
    languages = models.CharField(max_length=100)
    tsb = models.CharField(max_length=100)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=500)
