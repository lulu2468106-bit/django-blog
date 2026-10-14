from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        
        # This injects custom styling hooks straight into Django's form engine
        widgets = {
            'title': forms.TextInput(attrs={'class': 'cyber-input', 'placeholder': 'Enter post title...'}),
            'body': forms.Textarea(attrs={'class': 'cyber-input', 'rows': 8, 'placeholder': 'Write your content here...'}),
        }
