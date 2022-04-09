from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .backend import AuthBackend
from .models import *



def Register( request ) : 

    if request.method == 'POST' :

        #try :
                
        email = request.POST[ 'email' ]
        password = request.POST[ 'password' ]
        confirm_password = request.POST[ 'confirm_password' ]
        mobile = request.POST[ 'mobile' ]
        account = request.POST[ 'account' ]
        first_name = request.POST[ 'first_name' ]
        last_name = request.POST[ 'last_name' ]


        if password != confirm_password : 
            return render( request, 'register.html', { 'Message' : "Passwords Don't Match." } )

        elif User.objects.filter( email = email ).exists() : 
            return render( request, 'register.html', { 'Message' : "Account With This Email Address Already Exists." } )

        elif Student.objects.filter( mobile = mobile ).exists() : 
            return render( request, 'register.html', { 'Message' : "Account With This Mobile Number Already Exists." } )

        else :

            user = User( first_name = first_name, last_name = last_name, email = email )
            user.set_password( password )
            user.is_active = True
            user.save()

            if account == 'S' : 

                student = Student( user = user, mobile = mobile )
                student.save()
                return redirect( 'Login' )

            elif account == 'A' :

                user.is_staff = True
                user.is_superuser = True
                user.save()

                return redirect( 'http://localhost:8000/admin' )

            else : return render( request, 'register.html', { 'Message' : 'Account Type Not Selected.' } )

        #except Exception as e : return render( request, 'register.html', { 'Message' : str( e ) } )

    return render( request, 'register.html', {} )



def Login( request ) : 

    if request.method == 'POST' :

        email = request.POST[ 'email' ]
        password = request.POST[ 'password' ]

        try : 
            
            user = AuthBackend.authenticate( email = email, password = password )
            login( request, user )
            return redirect( 'http://localhost:8000/profile' )

        except Exception as e : return render( request, 'login.html', { 'Message' : e } )

    return render( request, 'login.html', {} )



def Logout( request ) :

    logout( request )
    return redirect( 'Login' )




def Profile( request ) : 

    if request.user.is_authenticated : 

        request.student = Student.objects.get( user = request.user )
        return render( request, 'profile.html', {} )

    return render( request, 'profile.html', { 'Message' : 'Login To View Your Profile' } )