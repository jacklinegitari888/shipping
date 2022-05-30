from http.client import responses
from multiprocessing import context
from tempfile import template
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


def index(request):
    latest_question_list=Question.objects.order_by("-pub_date")[:5]
    template=loader.get_template("index.html")
    context={"latest_question_list":latest_question_list,}
    return HttpResponse(template.render(context,request))
    