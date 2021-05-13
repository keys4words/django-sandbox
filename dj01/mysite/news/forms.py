from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Title', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Content', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6}))
    is_published = forms.BooleanField(label='Publication status', initial=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category', empty_label='Choose category', widget=forms.Select(attrs={'class':'form-select'}))