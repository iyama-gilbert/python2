# from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'home.html')
    # return HttpResponse('i am alreadyat home please')

def about(request):
    return render(request,'about.html')
    # return HttpResponse('my a bout page is here')
