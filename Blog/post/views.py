from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail

from .models import Post
from .forms import EmailPostForm
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


def post_share(request, post_id):
    #Recupra el post por el id
    post = get_object_or_404(Post, id=post_id, status='publicado')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #enviamos el correo
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = F"{cd['nombre']} {cd['apellido']} te recomendó leer {post.title}"
            message = F"Leer {post.title} en {post_url}\n\n comentarios de {cd['nombre']}: {cd['comentarios']}"
            send_mail(subject, message, 'daluz0221@gmail.com', [cd['para']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'post/share.html', {
        'post':post, 
        'form': form,
        'sent': sent
    })    
