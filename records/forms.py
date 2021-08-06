from django import forms
from .models import Publication
# from datetime import datetime
# from django.core.exceptions import ValidationError


class BookForm(forms.ModelForm):

    class Meta:
        model = Publication
        fields = '__all__'
        publication_date = forms.DateField(input_formats=['%Y-%m-%d'])

    # def clean_date(self, *args, **kwargs):
    #     date_passed = self.cleaned_data.get('publication_date')
    #     if date_passed != datetime.strptime(date_passed, "%Y-%m-%d").strftime('%Y-%m-%d'):
    #         raise ValidationError("Date format: Year-Month-Day")
    #     return date_passed


