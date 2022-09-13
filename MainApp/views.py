from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from MainApp.models import Snippet
from MainApp.forms import SnippetForm, UserRegistrationForm
from django.contrib import auth


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)

def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {'pagename': 'Добавление нового сниппета', 'form': form}
        return render(request, 'pages/add_snippet.html', context)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet=form.save()
            snippet.user = request.user
            snippet.save()
            return redirect("snippets")
        return render(request, 'add_snippet.html', {'form': form})

def snippets_page(request):
    snippets = Snippet.objects.all().filter(hidden=0)
    context = {'snippets': snippets}
    return render(request, 'pages/view_snippets.html', context)

def snippets_hidden(request):
    snippets = Snippet.objects.all().filter(hidden=1)
    context = {'snippets': snippets}
    return render(request, 'pages/view_snippets.html', context)

def snippets_all(request):
    snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    return render(request, 'pages/view_snippets.html', context)


def del_snippet_page(request, id):
    snippets = Snippet.objects.filter(id=id)
    snippets.delete()
    return redirect("snippets")

def snippet_detail(request, id):
    snippet = get_object_or_404(Snippet, id=id)
    context = {
        'pagename': 'Подробнее о сниппете',
        "snippet": snippet
    }
    return render(request, 'pages/snippet_details.html', context)


def upd_snippet_page(request, id):
    form_data = request.POST
    print(form_data)
    print(request.POST.get('flag_hide'))
    name = form_data["name"]
    lang = form_data["lang"]
    code = form_data["code"]
    creation_date = form_data['creation_date']
    snippet = Snippet.objects.filter(id=id)
    snippet.update(name=name,lang=lang,code=code,creation_date=creation_date)
    return redirect("snippets")

def login_page(request):
   if request.method == 'POST':
       username = request.POST.get("username")
       password = request.POST.get("password")
       # print("username =", username)
       # print("password =", password)
       user = auth.authenticate(request, username=username, password=password)
       if user is not None:
           auth.login(request, user)
       else:
           # Return error message
           pass
   return redirect('home')

def logout(request):
    auth.logout(request)
    return redirect('home')

def register(request):
    if request.method == "GET":
        form = UserRegistrationForm()
        context = {'pagename': 'Регистрация пользователя', "form": form}
        return render(request, 'pages/registration.html', context)
    if request.method == "POST":  # информацию от формы
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        context = {'pagename': 'Регистрация пользователя', "form": form}
        return render(request, 'pages/registration.html', context)