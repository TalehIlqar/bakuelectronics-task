
from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(
        self, username, password=None, is_active=True, is_staff=False, is_superuser=False
    ):
        if not username:
            raise ValueError("Users must have an username adress")
        user = self.model(username=username)
        user.set_password(password)
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.user_type = "manager"
        user.save(using=self._db)
        return user
