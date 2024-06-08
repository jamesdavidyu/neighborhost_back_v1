from django.db import models

class Zipcode(models.Model):
    zipcode_id                  = models.CharField(max_length=5, primary_key=True)
    city                        = models.CharField(max_length = 27)
    state                       = models.CharField(max_length = 35)

class Neighborhood(models.Model):
    neighborhood_id             = models.PositiveIntegerField(primary_key = True, default=0)
    neighborhood                = models.CharField(max_length = 255, default='Not assigned')
    neighborhood_found_when     = models.DateTimeField(auto_now_add = True)
