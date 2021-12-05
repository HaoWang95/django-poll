from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest
from django.urls import reverse
from .models import Choice, Question



def index(request: HttpRequest):
    print(request.get_full_path_info())
    question_list = Question.objects.order_by('-last_modified')[:5][::-1]
    context = {
        'question_list': question_list
    }
    return render(request, 'polls/index.html', context=context)


def detail(request: HttpRequest, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def result(request: HttpRequest, question_id):
    q = get_object_or_404(Question, pk=question_id)
    print(f'q in result view -> {result}')
    return render(request, 'polls/result.html', {'question': q})


def select(request: HttpRequest, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(f'q in select -> {question}')
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print(f'selected choice -> {selected_choice}')
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            'question': question,
            'error_message': "You did not select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))