from django.db import models
from Profiles.models import Student


class Question( models.Model ) : 

    id = models.AutoField( verbose_name = 'QUESTION ID', primary_key = True )
    question = models.CharField( verbose_name = 'QUESTION', max_length = 1024 )

    A = models.CharField( max_length = 128 )
    B = models.CharField( max_length = 128 )
    C = models.CharField( max_length = 128 )
    D = models.CharField( max_length = 128 )

    correct = models.CharField( verbose_name = 'Correct Choice', choices = [ ( 'A', 'A' ), ( 'B', 'B' ), ( 'B', 'B' ), ( 'B', 'B' ) ], max_length = 1 )
    difficulty = models.CharField( verbose_name = 'Difficulty Level', choices = [ ( 1, 'EASY' ), ( 2, 'MEDIUM' ), ( 3, 'HARD' ) ], max_length = 1 )



class PYTHON( Question ) : 

    class Meta : verbose_name_plural = 'PYTHON'

class JAVA( Question ) : 

    class Meta : verbose_name_plural = 'JAVA'

class OS( Question ) : 

    class Meta : verbose_name_plural = 'OS'

class DBMS( Question ) : 
    
    class Meta : verbose_name_plural = 'DBMS'

class CN( Question ) : 

    class Meta : verbose_name_plural = 'CN'





class Result( models.Model ) : 

    student = models.ForeignKey( Student, on_delete = models.PROTECT )
    subject = models.CharField( verbose_name = 'Subject', max_length = 32, choices = [ ( 'PYTHON', 'PYTHON' ), ( 'JAVA', 'JAVA' ), ( 'OS', 'OS' ), ( 'DBMS', 'DBMS' ), ( 'CN', 'CN' ) ], default = 'JAVA' )
    score = models.PositiveIntegerField( verbose_name = 'Score', default = 0)
    date = models.DateField( auto_now = True )

    responses = models.CharField( verbose_name = 'Responses', max_length = 256, default = '' )

    def __str__( self ) : return self.student.email + ' ' + self.date