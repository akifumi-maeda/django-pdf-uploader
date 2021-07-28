from django import forms
from .models import PdfUpload

class PdfUploadForm(forms.ModelForm):
    """PDFアップロードフォーム"""

    class Meta:
        model = PdfUpload
        fields = ('upload',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

from datetime import date, datetime

class QueryDateForm(forms.Form):
    """日付検索フォーム"""
    date = forms.DateField(
        label='日付',
        widget=forms.SelectDateWidget(
            attrs={'class': 'form-select'},
            years=range(datetime.today().year, datetime.today().year - 9, -1)
            )
        )

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class QueryDatePeriodForm(forms.Form):
    """日付期間検索フォーム"""
    error_css_class = 'error'

    start_period = forms.DateField(
        label='開始日',
        widget=forms.SelectDateWidget(
            attrs={'class': 'form-select'},
            years=range(datetime.today().year, datetime.today().year - 9, -1)
            )
        )
    end_period = forms.DateField(
        label='終了日',
        widget=forms.SelectDateWidget(
            attrs={'class': 'form-select'},
            years=range(datetime.today().year, datetime.today().year - 9, -1)
            )
        )

    def clean(self):
        cleaned_data = super().clean()
        start_period = cleaned_data.get('start_period')
        end_period = cleaned_data.get('end_period')

        if start_period and end_period:
            if start_period > end_period:
                raise ValidationError(_('開始日は完了日よりも前の日付に設定して下さい。'))