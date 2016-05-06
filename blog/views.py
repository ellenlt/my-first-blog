from django.shortcuts import render

# Create your views here.
def post_list(request):
	# Render function will take a request and render the template
	# Template name corresponds to the URL, 
	# so URL "blog/post_list.html" -> file in blog/template/blog/post_list.html
	return render(request, 'blog/post_list.html', {})