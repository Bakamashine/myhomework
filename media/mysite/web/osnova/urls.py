from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, zagl
urlpatterns  = [
    path('',index, name='home'),
    path('zaglushka/', zagl, name='zagl'),
] +  static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
