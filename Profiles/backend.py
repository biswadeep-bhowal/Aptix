from django.contrib.auth.backends import ModelBackend
from .models import User



class AuthBackend( ModelBackend ) : 

    def authenticate( email = None, password = None ) : 

        try : 

            user = User.objects.get( email = email )
            if user.check_password( password ) : return user
            else : raise Exception( 'Password Does Not Match...' )

        except Exception as e : raise Exception( str( e ) )