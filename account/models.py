from django.db import models
from django.contrib.auth.models import AbstractUser, User, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password):
        if not email:
            raise ValueError('The given email must be set')
        
        email = self.normalize_email(email)
        user = self.model(
			email=email,
		)
        user.set_password(password)
        user.save(using=self._db)

        return user

    
    def create_superuser(self, email, password):
        email = self.normalize_email(email)
        
        user = self.create_user(
			email=email,
			password=password,
		)

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractUser):
    username = models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and ./+/-/_ only.', max_length=150, unique=True, validators=[UnicodeUsernameValidator()], verbose_name='username', null=True)
    email = models.EmailField(verbose_name="email", max_length=255, unique=True)
    name = models.CharField(max_length=100)
    namausaha = models.CharField(max_length=100)
    kategori = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=200)
    address = models.TextField(null=True)
    kontak = models.CharField(max_length=100)
    linktoko = models.TextField(null=True)

    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    user = UserManager()

    def __str__(self):
        return "{}".format(self.email)
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True