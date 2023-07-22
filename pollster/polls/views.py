from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Models
from .models import Question, Choice

# Create your views here.
# Get question and display them
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context=context)

# Show specific question and choices
def detail(request, question_id):

    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question doesnot exists!')
    
    return render(request, 'polls/detail.html', {'question': question})


# Get question and display results
def results(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    
    return render(request, 'polls/results.html', {'question': question})