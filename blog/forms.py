from django import forms

from .models import Post

# Create a new form type for inputting a new Post
# forms.ModelForm tells Django that this form is a Model Form
class PostForm(forms.ModelForm):
	# Tells Django what model to use for form
    class Meta:
        model = Post
        fields = ('title', 'text',)