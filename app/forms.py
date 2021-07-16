from django.forms import ModelForm
from .models import PdfUpload

class PdfUploadForm(ModelForm):
    """PDFアップロードフォーム"""

    class Meta:
        model = PdfUpload
        fields = ('upload',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"