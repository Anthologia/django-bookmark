from django import forms
from .models import Bookmark

class BookmarkForm(forms.ModelForm):
    site_name = forms.CharField(label="사이트명")
    site_url = forms.CharField(label="주소")

    class Meta:
        model = Bookmark
        fields = '__all__'