from django.conf.urls import url
from . import views

# Stores information from url and assigns specific urls to views
urlpatterns = [
	# Assigning a view called post_list to an empty URL
	# The name of the URL is separate from the view name
	url(r'^$', views.post_list, name='post_list'),
	# The regexp ^post/(?P<pk>\d+)$ means that Django will take everything
	# after post/? and transfer to a view as a new variable called pk (primary key)
	# And \d tells us that it can only be a digit (so ignores the last backslash)
	url(r'^post/(?P<pk>\d+)$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit')
]