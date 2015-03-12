from django.shortcuts import render
from django.http.response import HttpResponse
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
