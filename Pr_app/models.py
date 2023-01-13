from django.db import models


# create new property

class Property_detail(models.Model):
    Pr_id = models.AutoField(primary_key=True)
    Property_name = models.CharField(max_length=100)
    Property_address = models.CharField(max_length=200)
    City_name = models.CharField(max_length=100)
    State_name = models.CharField(max_length=100)
