from django.shortcuts import render, redirect
from Profiles.models import User, Student
from .models import *



def Instructions( request ) : 

    if 'subject' in request.POST.keys() :   # RENDER INSTRUCTIONS PAGE 
        
        request.session[ 'subject' ] = request.POST[ 'subject' ]
        Initialise_Result( request )
        return render( request, 'instructions.html', { 'subject' : request.session[ 'subject' ] } )

    request = Initialise_Test( request )
    return redirect( 'http://localhost:8000/test/' )    # RENDER THE TEST


def Initialise_Result( request ) : 

    try : Result( student = Student.objects.get( user = request.user ), subject = request.session[ 'subject' ], score = 0 ).save()
    except Exception as e : raise Exception( e )


def Initialise_Test( request ) : 

    request.qno = 1
    request.difficulty = 1
    request.score = 0
    request.response = ""

    questions, question = [], Question()
    exec( "questions = list( {}.objects.all() )".format( request.session[ 'subject' ] ) )

    for q in questions :
        
        if q.difficulty == 1 :
            
            question = q
            questions.pop( questions.index( question ) )
            break

    request.questions = questions
    request.question = question

    return request



def Test( request ) :

    if 'option' not in request.POST.keys() : return render( request, 'question.html', {} )

    if request.POST[ 'option' ] == request.question.correct : # FOR CORRECT ANSWER
        request.score += request.question.difficulty
        if request.difficulty < 3 : request.difficulty += 1
    
    elif request.difficluty > 1 : request.difficulty -= 1

    request.response += '{}:{} '.format( request.question.id, request.POST[ 'option' ] )

    if request.qno == 10 : 
        redirect( 'http://localhost:8000/score' )
    
    request.qno += 1

    Q = request.questions
    q = request.question
    
    Q.pop( Q.index( q ) )
    
    for question in Q :
        if question.difficulty == request.difficulty : 
            q = question
            break

    request.questions = Q
    request.question = q

    return render( request, 'question.html', {} )










def Score( request ) : return render( request, 'score.html' )