from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations =True
    def create_user(self, email, username, phone, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")
        if not phone:
            raise ValueError("Phone number is required")

        # Normalize email address
        email = self.normalize_email(email)

        # Create and save the user with required fields
        user = self.model(email=email, username=username, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone, password=None, **extra_fields):
        # Create a superuser with required fields and additional permissions
        user = self.create_user(email, username, phone, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


    
class Users(AbstractBaseUser, PermissionsMixin):
    # Custom user model fields
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    referal_code  = models.CharField(max_length=100,blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Required for custom user model
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Define the field to be used as the unique identifier for logging in
    USERNAME_FIELD = 'email'
    # Additional fields required when creating a user
    REQUIRED_FIELDS = ['username', 'phone']

    # Custom user manager
    objects = UserManager()

    role = models.ForeignKey('Role', models.DO_NOTHING, default=None, null=False,blank=False,db_column='role_id')

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


# class UserRole(models.Model):
#     role = models.ForeignKey('Role', models.DO_NOTHING, null=False,blank=False,db_column='role_id')
#     user = models.ForeignKey('Users', models.DO_NOTHING, null=False,blank=False,db_column='user_id')
#     created_by = models.ForeignKey('Users', models.DO_NOTHING, null=False,blank=False,related_name='created_user',db_column='created_by')
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         managed = True
#         db_table = 'user_role'