from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import PdfUpload
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def index(request):
    return render(request, 'index.html')

class PdfUploadListView(generic.ListView):
    model = PdfUpload

class PdfUploadDetailView(generic.DetailView):
    model = PdfUpload

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PdfUploadForm

class PdfUploadCreateView(LoginRequiredMixin, CreateView):
    model = PdfUpload
    form_class = PdfUploadForm
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse('index')

class PdfUploadUpdateView(LoginRequiredMixin ,UpdateView):
    model = PdfUpload
    form_class = PdfUploadForm
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

class PdfUploadDeleteView(LoginRequiredMixin ,DeleteView):
    model = PdfUpload
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy('pdf_all')