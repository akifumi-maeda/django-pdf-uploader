from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.PdfUploadListView.as_view(), name='pdf_all'),
    path('pdf/<int:pk>', views.PdfUploadDetailView.as_view(), name='pdf_detail'),
    path('upload_pdf', views.PdfUploadCreateView.as_view(), name='upload_pdf'),
    path('pdf/<int:pk>/update/', views.PdfUploadUpdateView.as_view(), name='update_pdf'),
    path('pdf/<int:pk>/delete/', views.PdfUploadDeleteView.as_view(), name='delete_pdf'),
]