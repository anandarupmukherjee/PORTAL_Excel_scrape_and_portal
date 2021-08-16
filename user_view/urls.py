from django.urls import path
from .views import home, about,contact,result,search
 
urlpatterns = [
    path('', home, name = 'home'),
   path('about/', about, name = 'about'),
   path('contact/', contact, name = 'contact'), 
   path('result/', result, name = 'result'),
   path('search/', search, name = 'search'),

]
