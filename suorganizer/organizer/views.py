from django.shortcuts import render, get_object_or_404
from .models import Tag
from django.http.response import HttpResponse,Http404
from django.template import Context, loader
# Create your views here.


def homepage(request):
	return render(request,'organizer/tag_list.html',{'tag_list':Tag.objects.all()})

def tag_detail(request, slug):
	tag = get_object_or_404(Tag,slug__iexact=slug)
	return render(request,'organizer/tag_detail.html',{'tag':tag})
