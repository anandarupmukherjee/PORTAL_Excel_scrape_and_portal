# Create your views here.
from django.shortcuts import render
from .models import News, Empsearch
from django.template import RequestContext
#from django.shortcuts import render_to_response
import os, sys, subprocess
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm
from django.http import HttpResponseRedirect

from user_view.forms import UploadFileForm
from user_view.models import Profile



def SaveProfile(request):
   saved = False   
   if request.method == "POST":

      #Get the posted form
      MyProfileForm = UploadFileForm(request.POST, request.FILES)      
      if MyProfileForm.is_valid():
         profile = Profile()
         profile.name = MyProfileForm.cleaned_data["name"]
         profile.picture = MyProfileForm.cleaned_data["picture"]
         profile.save()
         saved = True
   else:
      MyProfileForm = Profileform()
   return render(request, 'about.html', locals())






def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['myfile'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'about.html', {'form': form})




def home(request):

   # obj = News.objects.all()
   # context = {"object":obj}
    return render(request, "home.html")


def about(request):
    msg=[]
    if request.method == 'POST' and 'run_script' in request.POST:
    # import function to run
       print("button click recieved")
       msg= os.system("python3 user_view/table_gen.py")


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


def search(request):
    return render(request, "search.html")


def index(request):
    return render(request, "index.html")



def result(request):
    result = News.objects.all()
    return render(request, 'result.html',{"Object":result})


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'templates/about.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'templates/home.html')



