from django.shortcuts import render
from .models import Blog
from django.views.generic.list import ListView
# Create your views here.


class BlogListView(ListView):
	model = Blog
	pagination_by = 5
	template_name = "blog/blog.html"

	