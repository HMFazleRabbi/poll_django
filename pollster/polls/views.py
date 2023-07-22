from django.shortcuts import render

# Models
from .models import Question, Choice

# Create your views here.
# Get question and display them
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context=context)