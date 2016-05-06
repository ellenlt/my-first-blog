from django.shortcuts import render
# Import model from the models file in the current directory
from .models import Post
# Because we use timezone in this file
from django.utils import timezone

# Create your views here.
def post_list(request):
	# Create a variable (aka name) for our QuerySet
	# lte = less than or equal to
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# Render function will take a request and render the template
	# Template name corresponds to the URL, so URL "blog/post_list.html" -> 
	# file in blog/template/blog/post_list.html
	# We also pass along the posts parameter to the view
	return render(request, 'blog/post_list.html', {'posts': posts})