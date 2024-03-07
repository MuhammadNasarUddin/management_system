from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    school = models.CharField(max_length=100)
    fb_link = models.URLField(max_length=350)

    OCCUPATION_CHOICES = [
        ('Facilitator', 'Facilitator'),
        ('Student', 'Student'),
        ('Staff', 'Staff'),
    ]

    occupation = models.CharField(max_length=12, choices=OCCUPATION_CHOICES)

    def __str__(self):
        return f"{self.username} - {self.school}"




class Interviews(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    interview_no =models.IntegerField()
    guest_name = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=550)

    def __str__(self):
        return f"{self.user.username} - {self.guest_name} - {self.topic}"
    



class Faceless(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    faceless_no =models.IntegerField()
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=550)

    def __str__(self):
        return f"{self.user.username} - {self.title}"



class Posting(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    posting_no = models.IntegerField()
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=550)


    def __str__(self):
        return f"{self.user.username} - {self.title}"
    


class Graphic(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    graphic_no = models.IntegerField()
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=550)

    def __str__(self):
        return f"{self.user.username} - {self.title}"