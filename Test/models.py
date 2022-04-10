from django.db import models
from Profiles.models import Student



class PYTHON( models.Model ) : 

    class Meta : verbose_name_plural = 'PYTHON'

    id = models.AutoField( verbose_name = 'QUESTION ID', primary_key = True, default = 1 )
    question = models.CharField( verbose_name = 'QUESTION', max_length = 1024, null = True )

    A = models.CharField( max_length = 128, null = True )
    B = models.CharField( max_length = 128, null = True )
    C = models.CharField( max_length = 128, null = True )
    D = models.CharField( max_length = 128, null = True )

    correct = models.CharField( verbose_name = 'Correct Choice', choices = [ ( 'A', 'A' ), ( 'B', 'B' ), ( 'C', 'C' ), ( 'D', 'D' ) ], max_length = 1, default = 'A' )
    difficulty = models.CharField( verbose_name = 'Difficulty Level', choices = [ ( 1, 'EASY' ), ( 2, 'MEDIUM' ), ( 3, 'HARD' ) ], max_length = 1, default = 1 )

    def __str__( self ) : return "{} : {}".format( self.id, self.difficulty )


class JAVA( models.Model ) : 

    class Meta : verbose_name_plural = 'JAVA'

    id = models.AutoField( verbose_name = 'QUESTION ID', primary_key = True, default = 1 )
    question = models.CharField( verbose_name = 'QUESTION', max_length = 1024, null = True )

    A = models.CharField( max_length = 128, null = True )
    B = models.CharField( max_length = 128, null = True )
    C = models.CharField( max_length = 128, null = True )
    D = models.CharField( max_length = 128, null = True )

    correct = models.CharField( verbose_name = 'Correct Choice', choices = [ ( 'A', 'A' ), ( 'B', 'B' ), ( 'C', 'C' ), ( 'D', 'D' ) ], max_length = 1, default = 'A' )
    difficulty = models.CharField( verbose_name = 'Difficulty Level', choices = [ ( 1, 'EASY' ), ( 2, 'MEDIUM' ), ( 3, 'HARD' ) ], max_length = 1, default = 1 )

    def __str__( self ) : return "{} : {}".format( self.id, self.difficulty )



class OS( models.Model ) : 

    class Meta : verbose_name_plural = 'OS'

    id = models.AutoField( verbose_name = 'QUESTION ID', primary_key = True, default = 1 )
    question = models.CharField( verbose_name = 'QUESTION', max_length = 1024, null = True )

    A = models.CharField( max_length = 128, null = True )
    B = models.CharField( max_length = 128, null = True )
    C = models.CharField( max_length = 128, null = True )
    D = models.CharField( max_length = 128, null = True )

    correct = models.CharField( verbose_name = 'Correct Choice', choices = [ ( 'A', 'A' ), ( 'B', 'B' ), ( 'C', 'C' ), ( 'D', 'D' ) ], max_length = 1, default = 'A' )
    difficulty = models.CharField( verbose_name = 'Difficulty Level', choices = [ ( 1, 'EASY' ), ( 2, 'MEDIUM' ), ( 3, 'HARD' ) ], max_length = 1, default = 1 )

    def __str__( self ) : return "{} : {}".format( self.id, self.difficulty )



class DBMS( models.Model ) : 
    
    class Meta : verbose_name_plural = 'DBMS'


    id = models.AutoField( verbose_name = 'QUESTION ID', primary_key = True, default = 1 )
    question = models.CharField( verbose_name = 'QUESTION', max_length = 1024, null = True )

    A = models.CharField( max_length = 128, null = True )
    B = models.CharField( max_length = 128, null = True )
    C = models.CharField( max_length = 128, null = True )
    D = models.CharField( max_length = 128, null = True )

    correct = models.CharField( verbose_name = 'Correct Choice', choices = [ ( 'A', 'A' ), ( 'B', 'B' ), ( 'C', 'C' ), ( 'D', 'D' ) ], max_length = 1, default = 'A' )
    difficulty = models.CharField( verbose_name = 'Difficulty Level', choices = [ ( 1, 'EASY' ), ( 2, 'MEDIUM' ), ( 3, 'HARD' ) ], max_length = 1, default = 1 )

    def __str__( self ) : return "{} : {}".format( self.id, self.difficulty )



class CN( models.Model ) : 

    class Meta : verbose_name_plural = 'CN'

    id = models.AutoField( verbose_name = 'QUESTION ID', primary_key = True, default = 1 )
    question = models.CharField( verbose_name = 'QUESTION', max_length = 1024, null = True )

    A = models.CharField( max_length = 128, null = True )
    B = models.CharField( max_length = 128, null = True )
    C = models.CharField( max_length = 128, null = True )
    D = models.CharField( max_length = 128, null = True )

    correct = models.CharField( verbose_name = 'Correct Choice', choices = [ ( 'A', 'A' ), ( 'B', 'B' ), ( 'C', 'C' ), ( 'D', 'D' ) ], max_length = 1, default = 'A' )
    difficulty = models.CharField( verbose_name = 'Difficulty Level', choices = [ ( 1, 'EASY' ), ( 2, 'MEDIUM' ), ( 3, 'HARD' ) ], max_length = 1, default = 1 )

    def __str__( self ) : return "{} : {}".format( self.id, self.difficulty )

    

class Result( models.Model ) : 

    student = models.ForeignKey( Student, on_delete = models.PROTECT )
    subject = models.CharField( verbose_name = 'Subject', max_length = 32, choices = [ ( 'PYTHON', 'PYTHON' ), ( 'JAVA', 'JAVA' ), ( 'OS', 'OS' ), ( 'DBMS', 'DBMS' ), ( 'CN', 'CN' ) ], default = 'JAVA' )
    score = models.PositiveIntegerField( verbose_name = 'Score', default = 0)
    date = models.DateField( auto_now = True )

    responses = models.CharField( verbose_name = 'Responses', max_length = 256, default = '' )

    def __str__( self ) : return str( self.student.get_user.email ) + ' ' + str( self.date )



class Cache( models.Model ) : 

    id = models.AutoField( verbose_name = 'CACHE ID', primary_key = True, default = 1 )

    student = models.ForeignKey( Student, on_delete = models.PROTECT )
    subject = models.CharField( verbose_name = 'Subject', max_length = 32, choices = [ ( 'PYTHON', 'PYTHON' ), ( 'JAVA', 'JAVA' ), ( 'OS', 'OS' ), ( 'DBMS', 'DBMS' ), ( 'CN', 'CN' ) ], default = 'JAVA' )
    score = models.PositiveIntegerField( verbose_name = 'Score', default = 0 )
    date = models.DateField( auto_now = True )

    r_1 = models.CharField( max_length = 16, null = True )
    r_2 = models.CharField( max_length = 16, null = True )
    r_3 = models.CharField( max_length = 16, null = True )
    r_4 = models.CharField( max_length = 16, null = True )
    r_5 = models.CharField( max_length = 16, null = True )
    r_6 = models.CharField( max_length = 16, null = True )
    r_7 = models.CharField( max_length = 16, null = True )
    r_8 = models.CharField( max_length = 16, null = True )
    r_9 = models.CharField( max_length = 16, null = True )
    r_10 = models.CharField( max_length = 16, null = True )

    question = models.CharField( max_length = 1024, null = True )
    qid = models.PositiveBigIntegerField( default = 1 )
    qno = models.PositiveIntegerField( default = 1 )

    A = models.CharField( max_length = 128, null = True )
    B = models.CharField( max_length = 128, null = True )
    C = models.CharField( max_length = 128, null = True )
    D = models.CharField( max_length = 128, null = True )    

    correct = models.CharField( choices = [ ( 'A', 'A' ), ( 'B', 'B' ), ( 'C', 'C' ), ( 'D', 'D' ) ], max_length = 1, default = 'A' )
    difficulty = models.PositiveIntegerField(  choices = [ ( 1, 'EASY' ), ( 2, 'MEDIUM' ), ( 3, 'HARD' ) ], default = 1 )

    def __str__( self ) : return str( self.student.user.get_email() )