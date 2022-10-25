from email import message
from django.shortcuts import render
from django.contrib import messages

from django.http import HttpResponseRedirect
from .forms import ContactForm
from .models import Profile, Projects, Skills, Work, Education,CvURL
from django.views.decorators.csrf import csrf_exempt
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import os


def portView(request):
    profile = Profile.objects.all()
    work = Work.objects.all()
    education = Education.objects.all()
    projects = Projects.objects.all()
    skills = Skills.objects.all()
    cf = ContactForm()
    link=CvURL.objects.all()
    
    return render(request, 'index.html', {'profile': profile, 'work': work, 'education': education, 'projects': projects, 'skills': skills, 'cf': cf,'link':link[0].url})


def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'Abhay__Resume.pdf'
    filepath = os.path.join(BASE_DIR, "Abhay__Resume.pdf")
    print("FILEPATH**_*")
    print(filepath)
    filename = os.path.basename(filepath)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(
        filepath, 'rb'), chunk_size), content_type=mimetypes.guess_type(filepath)[0])
    response['Content-Length'] = os.path.getsize(filepath)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def contact(request):
    profile = Profile.objects.all()
    work = Work.objects.all()
    education = Education.objects.all()
    projects = Projects.objects.all()
    skills = Skills.objects.all()
    link=CvURL.objects.all()
    
    print(request)
    print(request.method)
    if request.method == 'POST':
        cf = ContactForm(request.POST)
        if cf.is_valid():
            cf.save()
            messages.success(request, 'Message sent successfully!')
            return HttpResponseRedirect('/')
    else:
        cf = ContactForm()
    return render(request, 'index.html', {'profile': profile, 'work': work, 'education': education, 'projects': projects, 'skills': skills, 'cf': cf,'link':link[0].url})
