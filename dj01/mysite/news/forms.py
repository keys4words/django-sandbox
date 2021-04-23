from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Title')
    content = forms.CharField(label='Content', required=False)
    is_published = forms.BooleanField(label='Publication status', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category', empty_label='Choose category')