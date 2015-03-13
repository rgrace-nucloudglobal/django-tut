from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
# , Http404
from django.core.urlresolvers import reverse
from polls.models import Question
from django.template import RequestContext, loader
from models import Choice
# from django.views.generic.list import ListView
from django.views import generic

# Create your views here.

def index(request):
    # basic example    return HttpResponse("Hey ! you're at the Polls home
    # page.")

    # this group just prints out a list of existing questions
    #     latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #     output = ','.join([p.question_text for p in latest_question_list])
    #     return HttpResponse(output)

    # this group consumes a template to display the same list as above
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(
    #     request, {'latest_question_list': latest_question_list})
    # return HttpResponse(template.render(context))

    # yet another optimization
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # initial basic handling that i glazed over before
    # return HttpResponse("You are looking at question %s." % question_id)

    # explicit calls to get question or throw an exept
    #     try:
    #         question = Question.objects.get(pk=question_id)
    #     except Question.DoesNotExist:
    #         raise Http404('Question does not exist.')
    #     return render(request, 'polls/detail.html', {'question': question})

    # shortcut to the above
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    # response = "You are on the results page for question %s."
    # return HttpResponse(response % question_id)

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    # return HttpResponse("You are on the voting page for question %s." %
    # question_id)
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You did not select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # allways return an HttpResponseRedirect after successful handling POST data.
        # Prevents double-submission after back-button navigation
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
