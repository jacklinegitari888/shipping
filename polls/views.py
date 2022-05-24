from http.client import responses
from django.shortcuts import render
from django.http import HttpResponse
import time
from .models import Question
from django.template import loader


# Create your views here.


def get_questions(request):
    ## stuff 
    questions=Question.objects.all()
    template=loader.get_template("index.html")
    context={"latest_question_list":questions}
    return HttpResponse(template.render(context,request))

def get_question(request,id):
    question=Question.objects.get(pk=id)
    if question:
        template=loader.get_template("index.html")
        context={"latest_question_list":[question]}
        return HttpResponse(template.render(context,request))
    return HttpResponse("Question with id "+str(id)+ "not available")
    

def get_time(request):
    now=f"it is now {time.localtime()}"     
    return HttpResponse(now)
def get_detail(request, question_id):
    return HttpResponse("you are looking at question %s." % question_id)
def get_results(request, question_id):
    response="you are looking at results of question %s "
    return HttpResponse(response % question_id)
def get_vote(request, question_id):
    return HttpResponse("you are voting on question %s." % question_id)
    