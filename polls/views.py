from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse, Http404

from .models import Question, Choice


'''def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def index(request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, 'polls/index.html', context)'''

    #output = ', '.join([q.question_text for q in latest_question_list])


'''def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Pergunta nao existe!")
    return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("Voce esta procurando a questao %s" % question_id)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})'''


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        choice__choice_text__isnull = False
        Question.objects.
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Escolhe ai, boy.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #print reverse('polls:results', args=(question.id,))
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



