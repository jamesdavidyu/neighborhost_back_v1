from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
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
    
class Neighbor(AbstractBaseUser, PermissionsMixin):
    neighbor_id         = models.PositiveBigIntegerField(primary_key=True)
    signup_datetime     = models.DateTimeField(auto_now_add=True)
    username            = models.CharField(max_length=30, unique=True)
    email               = models.EmailField(unique=True)
    zipcode             = models.ForeignKey(Zipcode, on_delete=models.CASCADE)
    verified            = models.BooleanField(default=False)
    neighborhood        = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, default=0)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_admin            = models.BooleanField(default=False)
    
    def get_full_name(self):
        pass

    def get_short_name(self):
        pass

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
       return self.is_admin

    def has_perm(self, perm, obj=None):
       return self.is_admin

    def has_module_perms(self, app_label):
       return self.is_admin

    @is_staff.setter
    def is_staff(self, value):
        self._is_staff = value

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