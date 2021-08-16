# Create your views here.
from django.shortcuts import render
from .models import News, Empsearch
from django.template import RequestContext
#from django.shortcuts import render_to_response
import os, sys, subprocess



def home(request):

   # obj = News.objects.all()
   # context = {"object":obj}
    return render(request, "home.html")


def about(request):
    msg=[]
    if request.method == 'POST' and 'run_script' in request.POST:
    # import function to run
       print("button click recieved")
       msg= os.system("python3 user_view/test.py")


    if msg == 0:
        var="Database update success"
    else:
        var="Error"   
       #os.system("deactivate")
    #  subprocess.call([sys.executable, table_gen.py])
    #  os.system("python3 user_view/table_gen.py")
    # return user to required page

    return render(request, "about.html", {"obj":var})

def contact(request):
#    search_term = ''
#
#    if 'search' in request.GET:
#        search_term = request.GET['search']
#        print(search_term)
#    obj = News.objects.all().filter(name='UB.xlsx')
    obj= News.objects.all().filter(name='UB.xlsx')
    context = {"object":obj}
    return render(request, "contact.html", context)


def result(request):
    return render(request, "result.html")


def search(request):
    result = News.objects.all()
    return render(request, 'result.html',{"Object":result})
