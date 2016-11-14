from django.shortcuts import render, Http404, get_object_or_404

from .models import Question, Answer
from .forms import UserResponseForm


def single(request, id):
    if request.user.is_authenticated():
        form = UserResponseForm(request.POST or None)
        if form.is_valid():
            question_id = form.cleaned_data.get('question_id')
            answer_id = form.cleaned_data.get('answer_id')
            question_instance = Question.objects.get(id=question_id)
            answer_instance = Answer.objects.get(id=answer_id)
        title = 'Question'
        queryset = Question.objects.all().order_by('-timestamp')
        instance = get_object_or_404(Question, id=id)
        context = {'qs': queryset,
                   'title': title,
                   'instance': instance,
                   'form': form,
                   }
        return render(request, 'question/question_home.html', context)
    else:
        raise Http404



def home(request):
    if request.user.is_authenticated():
        form = UserResponseForm(request.POST or None)
        if form.is_valid():
            print form.cleaned_data
        title = 'Question'
        queryset = Question.objects.all().order_by('-timestamp')
        instance = queryset[0]
        context = {'qs': queryset,
                   'title': title,
                   'instance': instance,
                   'form': form,
                   }
        return render(request, 'question/question_home.html', context)
    else:
        raise Http404
