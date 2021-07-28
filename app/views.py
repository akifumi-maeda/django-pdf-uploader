from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import PdfUpload
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def index(request):
    return render(request, 'index.html')

from .forms import QueryDateForm, QueryDatePeriodForm

class PdfUploadListView(generic.ListView):
    model = PdfUpload
    paginate_by = 1

    def get_queryset(self):
        # 検索ワードの取得
        query = self.request.GET.get('query')

        # 検索日の取得
        query_year = self.request.GET.get('date_year')
        query_month = self.request.GET.get('date_month')
        query_day = self.request.GET.get('date_day')

        # 検索期間の取得
        query_start_year = self.request.GET.get('start_period_year')
        query_start_month = self.request.GET.get('start_period_month')
        query_start_day = self.request.GET.get('start_period_day')
        query_end_year = self.request.GET.get('end_period_year')
        query_end_month = self.request.GET.get('end_period_month')
        query_end_day = self.request.GET.get('end_period_day')

        if query:
            object_list =  PdfUpload.objects.filter(upload__icontains=query)
        elif query_year and query_month and query_day:
            object_list = PdfUpload.objects.filter(upload_date__year=query_year, upload_date__month=query_month, upload_date__day=query_day)
        elif query_start_year and query_start_month and query_start_day and query_end_year and query_end_month and query_end_day:
            from datetime import date
            start_date = date(int(query_start_year), int(query_start_month), int(query_start_day))
            end_date = date(int(query_end_year), int(query_end_month), int(query_end_day))
            object_list = PdfUpload.objects.filter(upload_date__range=(start_date, end_date))
        else:
            object_list = PdfUpload.objects.all()
        # セッションに入力データを格納
        # self.request.session['form_data'] =self.request.GET
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query_date_form'] = QueryDateForm(self.request.GET)
        context['query_date_period_form'] = QueryDatePeriodForm(self.request.GET)
        if self.request.GET.get('query'):
            context['query_value'] = self.request.GET.get('query')
        else:
            context['query_value'] = None
        return context

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
        return reverse('pdf_all')

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