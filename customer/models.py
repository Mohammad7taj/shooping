from django.db import models
from django.contrib.auth.hashers import make_password, check_password

import uuid



class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, verbose_name="نام کاربری")
    password = models.CharField(max_length=20, verbose_name="رمز عبور") 
    fname = models.CharField(max_length=35, verbose_name="نام")
    lname = models.CharField(max_length=35, verbose_name="نام خانوادگی")

    def set_password(self, raw_password: str):
        self.password = make_password(raw_password)  

    def check_password(self, raw_password: str) -> bool:
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return self.username

    
