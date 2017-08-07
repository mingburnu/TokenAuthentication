from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView

from .models import Choice, Question


def index(request):
    template_name = 'polls/index.html'
    questions = Question.objects.all()

    context = {
        "questions": questions
    }
    return render(request, template_name, context)


class Detail(DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get(self, request, *args, **kwargs):
        question = get_object_or_404(self.model, pk=self.kwargs['pk'])
        return render(request, self.template_name, {'question': question})


class Results(DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get(self, request, *args, **kwargs):
        question = get_object_or_404(self.model, pk=self.kwargs['pk'])

        return render(request, self.template_name, {'question': question})


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
