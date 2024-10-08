from django.shortcuts import HttpResponse, render
from .models import Question
from django.http import Http404
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "index.html", context) 
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "detail.html", {"question": question})
def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s" %question_id)
def vote(request, question_id):
    return HttpResponse("You're voting on question %s" %question_id)