from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be more than two characters."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be more than two characters."

        try:
            validate_email(postData['email'])
        except ValidationError:
            errors['email'] = "Email is not valid."
        # else:
        #     if User.objects.get(email=postData['email']):
        #         errors['email'] = "Email is already in use."

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()