from django.contrib.auth.models import AbstractUser
from django.db import models



class User( AbstractUser ) : 

    username = None
    email = models.EmailField( verbose_name = 'Email Address', default = 'email@email.com', primary_key = True )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__( self ) : return self.email



class Student( models.Model ) : 

    user = models.OneToOneField( User, on_delete = models.PROTECT )
    mobile = models.CharField( verbose_name = 'Mobile Number', max_length = 10, default = '0000000000' )

    def __str__( self ) : return self.user.email
