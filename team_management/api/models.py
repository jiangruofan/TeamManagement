from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, null=False)
    email = models.EmailField(null=False)
    is_admin = models.BooleanField(null=False)

