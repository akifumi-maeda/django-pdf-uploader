import os
from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class PdfUpload(models.Model):
    upload  = models.FileField(
        upload_to='uploads/%Y/%m/%d',
        verbose_name='添付ファイル',
        validators=[FileExtensionValidator(['pdf',])],
        null=True
    )
    upload_date = models.DateField(auto_now=True)

    def file_name(self):
        path = os.path.basename(self.upload.name)  # ファイル名のみ抽出
        return path