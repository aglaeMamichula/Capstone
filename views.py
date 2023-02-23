from django.shortcuts import render

# Create your views here.  
def home(request):
    """Get home html

        :param request: The request object used to generate this response

        :returns: HttpResponse

        :rtype: HttpResponse 
    """
    return render(request, "home.html")
  
def projects(request):
    """Get projects html

        :param request: The request object used to generate this response

        :returns: HttpResponse

        :rtype: HttpResponse 
    """
    return render(request, "projects.html")
  
def contact(request):
    """Get contact html

        :param request: The request object used to generate this response

        :returns: HttpResponse

        :rtype: HttpResponse 
    """
    return render(request, "contact.html")
    
def login(request):
    """Get login html

        :param request: The request object used to generate this response

        :returns: HttpResponse

        :rtype: HttpResponse 
    """
    return render(request, "registration/login.html")