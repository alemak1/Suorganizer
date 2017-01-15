from django.shortcuts import render
from .models import Tag
from django.http.response import HttpResponse
# Create your views here.


def homepage(request):
	tag_list = Tag.objects.all()
	output = ", ".join([tag.name for tag in tag_list])
	return HttpResponse(output)