from django import forms
from test_app.models import MarketData


class MarketDataForm(forms.ModelForm):
    class Meta:
        model = MarketData
        fields = ['ticker']
