from django.shortcuts import render
from .forms import CreatePollForm
from django.http import HttpResponse

# Create your views here.

def home(request):
    """Get polls/home html

        :param request: The request object used to generate this response

        :returns: HttpResponse

        :rtype: HttpResponse 
    """
    context = {}
    return render(request, 'poll/home.html', context)

def create(request):
    """Get polls/create html

        :param request: The request object used to generate this response

        :returns: HttpResponse

        :rtype: HttpResponse 
    """
    context = {}
    return render(request, 'poll/create.html', context)

def results(request):
    """Get polls/results html

        :param request: The request object used to generate this response

        :returns: HttpResponse

        :rtype: HttpResponse 
    """
    context = {}
    return render(request, 'poll/results.html', context)

def vote(request):
    """Get polls/vote html

        :param request: The request object used to generate this response

        :returns: HttpResponse

        :rtype: HttpResponse 
    """
    context = {}
    return render(request, 'poll/vote.html', context)
    
def create(request):
    """Get polls/create html

        :param request: The request object used to generate this response

        :returns: HttpResponse

        :rtype: HttpResponse 
    """
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
    else:
        form = CreatePollForm()

    context = {'form' : form}
    return render(request, 'poll/create.html', context)