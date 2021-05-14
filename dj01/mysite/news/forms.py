from django import forms
from .models import Category, News



class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields =['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.Select(attrs={'class':'form-select'})
        }



# class NewsForm(forms.Form):
    # title = forms.CharField(max_length=150, label='Title', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # content = forms.CharField(label='Content', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6}))
    # is_published = forms.BooleanField(label='Publication status', initial=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category', empty_label='Choose category', widget=forms.Select(attrs={'class':'form-select'}))
