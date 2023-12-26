from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from blokapp.models import Post


# Create your views here.
def index(request):
    name = request.user
    posts = Post.objects.all()

    context = {'name': name, 'posts': posts}
    return render(request, 'index.html', context)


def store(request):
    if request.method == 'POST':
        rpost = request.POST

        if rpost['title'] == '' or rpost['content'] == '':
            messages.error(request, 'Erro ao salvar o post!')
            return redirect('store')

        post = Post(title=rpost['title'], content=rpost['content'])
        Post.save(post)

        messages.success(request, 'Operação realizada com sucesso!')
        return redirect('index')

    if not request.user.is_authenticated:
        messages.error(request, 'Por favor, realize login para continuar!')
        return redirect('login')

    return render(request, 'store.html')


def login(request):
    if request.method == 'POST':
        rpost = request.POST
        user = authenticate(username=rpost['username'], password=rpost['password'])
        if user is None:
            messages.error(request, 'Usuário ou senha inválidos!')
            return redirect('login')

        auth_login(request, user)
        return redirect('index')

    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        rpost = request.POST
        if rpost['username'] == '' or rpost['email'] == '' or rpost['password'] == '':
            messages.error(request, 'Erro ao salvar o usuário!')
            return redirect('signup')
        if rpost['password'] != rpost['cpassword']:
            messages.error(request, 'As senhas não concidem!')
            return redirect('signup')

        User.objects.create_user(rpost['username'], rpost['email'], rpost['password'])
        messages.success(request, 'Por favor, realize login para continuar!')
        return redirect('login')

    if request.user.is_authenticated:
        return redirect('index')

    return render(request, 'signup.html')


def logout(request):
    auth_logout(request)
    messages.success(request, 'Logout realizado com sucesso!')

    return redirect('login')
