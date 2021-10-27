from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .models import Post
# Create your views here
# 
#.

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'post/list.html'


def post_detail(request, year, month, day, post):

    post = get_object_or_404(Post, slug=post, status='publicado', publish__year=year,publish__month=month, publish__day=day)

    return render(request, 'post/detail.html', {'post':post})
