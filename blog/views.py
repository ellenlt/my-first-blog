from django.shortcuts import render, get_object_or_404
# Import model from the models file in the current directory
from .models import Post
# Because we use timezone in this file
from django.utils import timezone
# For the post_new view
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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
	#username = None
	#if request.user.is_authenticated():
	# get_object_or_404 is a built in Django function that handles the case where
	# no pk was passed in
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
	# The case where you just submitted info on the form
	# and have returned to this view. Now there is
	# info in the request.POST which we want to save
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	# The case where you are first visiting this view
	else:
		form = PostForm()
		return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	# Users can only edit their own posts
	if request.user != post.author:
		return redirect('django.contrib.auth.views.login')
	elif request.method == "POST":
		# Pass the post as an instance when we save it
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		# Pass the post as an instance when we open it up
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})
