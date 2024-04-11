from django.db import models

# Create your models here.

class Users(models.Model):
    USER_ID = models.AutoField(primary_key=True)
    class Meta:
        db_table = 'aquafinder.users'


class Transactions (models.Model):

    CUSTOMER_ID = models.ForeignKey(Users, on_delete=models.CASCADE, to_field = 'USER_ID')

    class Meta:
        db_table = 'aquafinder.transations'
        

# class Sellers:
#     pass

# class Reviews:
#     pass
# class Productfeed:
#     pass












































#class users(models.Model):
#     user_id = models.AutoField(primary_key= True)
#     user_name = models.CharField(max_length = 50)
#     email = models.CharField(max_length = 100)  
#     password = models.CharField(max_length = 100)
#     first_name = models.CharField(max_length = 50)
#     last_name = models.CharField(max_length = 50)
#     dob = models.DateField
#     gender = models.CharField(
#         max_length=1,
#         choices=[
#             ('M', 'Male'),
#             ('F', 'Female'),
#         ]
#     )
#     address = models.CharField(max_length = 100)
#     phone_number = models.CharField(max_length = 10)
#     account_date = models.DateField
#     last_login = models.DateField
#     account_status = models.CharField(
#         max_length=1,
#         choices=[
#             ('A' 'Active'),
#             ('D', 'Deactivated'),
#         ]
#     )
#     role = models.CharField(
#         max_length=1,
#         choices=[
#             ('A' 'Admin'),
#             ('U', 'User'),
#         ]
#     )
#     profile_icon = address = models.CharField(max_length = 500)



# class subscriptions (models.Model):
#     cutomer_id = 
#     sub_id = models.AutoField(primary_key= True)
#     sub_start = models.DateField
#     sub_end = models.DateField
#     sub_status =  account_status = models.CharField(
#         max_length=1,
#         choices=[
#             ('A' 'Active'),
#             ('D', 'Stopped'),
#         ]
#     )
#     payment_method =  account_status = models.CharField(
#         max_length=8,
#         choices=[
#             ('Card' ''),
#             ('PayPal', ''),
#             ('Contract', '')
#         ]
#     )
#     payment_status = 
#     billing_adress =
#     auto_renewal =
#     support_requests =


