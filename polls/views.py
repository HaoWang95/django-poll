from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Question

# Create your views here.

def index(request: HttpRequest):
    print(request.get_full_path_info())
    question_list = Question.objects.order_by('-last_modified')[:5]
    context = {
        'question_list': question_list
    }
    return render(request, 'polls/index.html', context=context)


def detail(request: HttpRequest, question_id):
    question = Question.objects.filter(id=question_id)
    response = f'Detail page for question {question_id} - {question.get()}'
    return HttpResponse(response)


def result(request: HttpRequest, question_id):
    response = f'Results of question {question_id}'
    return HttpResponse(response)


def select(request: HttpRequest, question_id):
    response = f'Select on question: {question_id}'
    return HttpResponse(response)
