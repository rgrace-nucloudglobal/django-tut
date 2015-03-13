from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, Http404
from polls.models import Question
from django.template import RequestContext, loader
# Create your views here.

def index(request):
    # basic example    return HttpResponse("Hey ! you're at the Polls home
    # page.")

    # this group just prints out a list of existing questions
    #     latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #     output = ','.join([p.question_text for p in latest_question_list])
    #     return HttpResponse(output)

    # this group consumes a template to display the same list as above
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(
        request, {'latest_question_list': latest_question_list})
    return HttpResponse(template.render(context))

def detail(request, question_id):
    # explicit calls to get question or throw an exept
    #     try:
    #         question = Question.objects.get(pk=question_id)
    #     except Question.DoesNotExist:
    #         raise Http404('Question does not exist.')
    #     return render(request, 'polls/detail.html', {'question': question})

    # shortcut to the above
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
