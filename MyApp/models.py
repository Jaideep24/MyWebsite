from django.db import models

# Create your models here.
class Weather_city(models.Model):
    city=models.TextField()
    def __str__(self):
        return(self.city)
class Login(models.Model):
    email_id=models.EmailField(default="email@example.com")
    password=models.TextField()
    def __str__(self):
        return(self.email_id)
class Sign_Up(models.Model):
    username=models.TextField(default="example")
    email_id=models.EmailField()
    password=models.TextField()
    USERNAME_FIELD = 'username'
    def __str__(self):
        return(self.email_id)