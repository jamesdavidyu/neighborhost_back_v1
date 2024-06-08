from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from api.models import Zipcode
from api.models import Neighborhood

class NeighborManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('You must provide an email to create an account. Please try again.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class Neighbor(AbstractBaseUser):
    neighbor_id     = models.PositiveBigIntegerField(primary_key=True)
    signup_datetime = models.DateTimeField(auto_now_add=True)
    username        = models.CharField(max_length=30, unique=True)
    email           = models.EmailField(unique=True)
    zipcode         = models.ForeignKey(Zipcode, on_delete=models.CASCADE)
    verified        = models.BooleanField(default=False)
    neighborhood    = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, default=0)
    is_active       = models.BooleanField(default=True)
    _is_staff       = models.BooleanField(default=False)

    objects = NeighborManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'zipcode']

class Addresse(models.Model):
    address_id      = models.PositiveBigIntegerField(primary_key=True)
    neighbor        = models.ForeignKey(Neighbor, on_delete=models.CASCADE)
    first_name      = models.CharField(max_length=35)
    last_name       = models.CharField(max_length=35)
    address         = models.CharField(max_length=50)
    city            = models.CharField(max_length=27)
    state           = models.CharField(max_length=35)
    neighborhood    = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)