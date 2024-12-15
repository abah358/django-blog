from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blogging.models import Post
from django.template import loader


# Create your views here.
class BlogListView(ListView):
    model = Post
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
    template_name = 'blogging/list.html'


class BlogDetailView(DetailView):
    model = Post
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
    template_name = 'blogging/detail.html'

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        context = {'post': post}
        return render(request, 'blogging/detail.html', context)
