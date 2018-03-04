# Create your models here


from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from post.utils import rand_uid
# from post.models import Post

class UserProfileManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, bio=None, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        if not first_name:
            raise ValueError("Users must have first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        user = self.model(
            email = self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            bio=bio
        )
        user.set_password(password)
        # user.staff = is_staff
        # user.admin = is_admin
        # user.active = is_active
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, last_name , bio=None, password=None):
        user = self.create_user(
            email,
            first_name, 
            last_name,
            bio=bio,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, bio=None, password=None):
        user = self.create_user(
            email, 
            first_name, 
            last_name,
            bio=bio,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True) 
    bio = models.CharField(max_length=255, blank=True, null=True)   
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    uid = models.CharField(max_length=8, unique=True)
    # profile_pic = models.ImageField(default='guest-user.png', upload_to='ProfilePic', blank=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserProfileManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + self.last_name

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    
def get_uid(instance, uid=None):
    _uid = rand_uid()
    if uid is not None:
        _uid = uid
    qs = UserProfile.objects.filter(uid=_uid)
    exists = qs.exists()
    if exists:
        _uid = rand_uid()
    return _uid

def user_pre_save(signal, instance, sender, **kwargs):
    if not instance.uid:
        instance.uid = get_uid(instance)


pre_save.connect(user_pre_save, sender=UserProfile)