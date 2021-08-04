import os
from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse

# Create your models here.

class PdfUpload(models.Model):
    upload  = models.FileField(
        upload_to='uploads/%Y/%m/%d',
        verbose_name='添付ファイル',
        validators=[FileExtensionValidator(['pdf',])],
    )
    upload_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['upload_date']

    def __str__(self):
        """ファイルのURLを返す"""
        return self.file.url

    def get_absolute_url(self):
        """モデルの詳細レコードのurlを返す"""
        return reverse("pdf_detail", kwargs={"pk": self.pk})

    def file_name(self):
        """ファイルのurlからファイル名のみ返す"""
        path = os.path.basename(self.upload.name)
        return path