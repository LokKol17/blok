from django.shortcuts import render, redirect

from blokapp.models import Post


# Create your views here.
def index(request):
    name = 'Lokkol17'
    posts = Post.objects.all()

    context = {'name': name, 'posts': posts}
    return render(request, 'index.html', context)


def store(request):
    if request.method == 'POST':
        rpost = request.POST
        post = Post(title=rpost['title'], content=rpost['content'])
        Post.save(post)

        return redirect('index')

    return render(request, 'store.html')
