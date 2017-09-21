from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'upload', views.upload_file, name='upload_file'),
    url(r'list', views.list_files, name='list_files'),
    url(r'download/([0-9]*)$', views.download_file, name='download_file'),
]
