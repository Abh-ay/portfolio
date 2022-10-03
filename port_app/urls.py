from importlib.resources import path


from django.urls import path
from . import views
urlpatterns = [
    path('', views.portView),
    path('download/', views.download_file, name='download_file'),
    path('contact/', views.contact, name='contact_me')

]
