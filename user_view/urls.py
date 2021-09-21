from django.urls import path
from .views import home, about,contact,result,search, index
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
   path('', index, name = 'index'),
   path('home/', home, name = 'home'),
   path('about/', about, name = 'about'),
   path('contact/', contact, name = 'contact'), 
   path('result/', result, name = 'result'),
   path('search/', search, name = 'search'),


]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




