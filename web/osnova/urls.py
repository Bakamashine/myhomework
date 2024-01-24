from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, zagl
from django.views.generic import TemplateView
urlpatterns  = [
    path('',index, name='home'),
    path('zaglushka/', zagl, name='zagl'),
    path('static/style.css', TemplateView.as_view(template_name='style.css', content_type='text/css')),
] +  static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
