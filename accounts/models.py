from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.core.mail import send_mail
# Create your models here.

class User(AbstractUser):

    phone = models.CharField(max_length=200,unique=True)

    ROLE_CHOICE = {
        ("student","student"),
        ("admin","admin")
    }

    role = models.CharField(max_length=200,choices=ROLE_CHOICE,default="student")

class StudentProfile(models.Model):
    
    skills = models.CharField(max_length=200,null=True)
    
    qualification = models.CharField(max_length=200,null=True)

    passout_year = models.CharField(max_length=200,null=True)

    github_url = models.URLField(null=True)

    linkedin_url = models.URLField(null=True)

    student = models.OneToOneField(User,on_delete=models.CASCADE,related_name="student")

def created_student_profile(sender,instance,created,*args,**kwargs):

    if created and instance.role == "student":

        StudentProfile.objects.create(student=instance)


post_save.connect(created_student_profile,sender=User)


def send_invitation_mail(sender,instance,created,*args,**kwargs):

    if created and instance.role == "student":
        
        send_mail(
            
            "you have successfully created email",
            "you have successfullu created accounts in codepilot",
            "godwinfranco87@gmail.com",
            ["to@example.com"],

            )

post_save.connect(send_invitation_mail,sender=User)