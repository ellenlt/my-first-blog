from django.shortcuts import render, get_object_or_404
# Import model from the models file in the current directory
from .models import Post
# Because we use timezone in this file
from django.utils import timezone


# Create your views here.
# Tells Django what variables to pass to the view
# and renders the view
def post_list(request):
	# Create a variable (aka name) for our QuerySet
	# lte = less than or equal to
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# Render function will take a request to display a view (post_list)
	# and render the corresponding template (post_list.html).
	# Usually template names match view names
	# We also pass along the posts parameter to the view
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	# get_object_or_404 is a built in Django function that handles the case where
	# no pk was passed in
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

