from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '할 일을 입력해주세요'}),
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '세부 내용을 입력해주세요'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title or len(title.strip()) == 0:
            raise forms.ValidationError("할 일 제목을 입력해주세요.")
        return title