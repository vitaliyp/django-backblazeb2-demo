from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from wsgiref.util import FileWrapper

import mimetypes
import os.path

from .forms import UploadFileForm
from .models import JustFile

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(request.FILES)
        print(form.errors)
        if form.is_valid():
            a = JustFile()
            a.myfile = request.FILES['myfile']
            a.size = a.myfile.size
            a.save()
            return HttpResponseRedirect('/testapp/list')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def list_files(request):
    files = JustFile.objects.all()
    return render(request, 'list.html', {'files': files})

def download_file(request, file_id):
    if request.method == 'GET':
        f = JustFile.objects.get(id=file_id)
        file_wrapper = FileWrapper(f.myfile)
        file_mimetype = mimetypes.guess_type(f.myfile.url)
        response = HttpResponse(file_wrapper, content_type=file_mimetype)
        response['X-Sendfile'] = f.myfile.name
        response['Content-Length'] = f.size
        response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(f.myfile.name)
        return response
