#from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def list_books(request):
#   return HttpResponse("We could put anything here")
#   return HttpResponse(request.user.username)
    return render(request, "list.html")