from django.shortcuts import render

# Models
from .models import Question, Choice

# Create your views here.
# Get question and display them
def index(request):
    return render(request, 'polls/index.html')