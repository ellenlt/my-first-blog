from django.conf.urls import url
from . import views

urlpatterns = [
	# Assigning a view called post_list to an empty URL
	# The name of the URL is separate from the view name
	url(r'^$', views.post_list, name='post_list'),
]