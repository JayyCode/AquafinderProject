from django.db import models

# Create your models here.
class users(models.Model):
    title = models.AutoField(primary_key= True)
    user_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)  
    password = models.CharField(max_length = 100)
    # first_name = models.
    # last_name =
    # dob =
    # gender = 
    # address =
    # phone_number = 
    # account_date =
    # last_login =
    # account_status =
    # role =
    # profile_icon = 
