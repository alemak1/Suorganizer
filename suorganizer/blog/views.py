from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.

def post_list(request):
	return render(request,'blog/post_list.html',{'post_list':Post.objects.all()})

def post_detail(request):
	post = get_object_or_404(
		Post,
		pub_date__year=year,
		pub_date__month=month,
		slug=slug)
	return render(
		request,
		'blog/post_detail.html',
		{'post':post})