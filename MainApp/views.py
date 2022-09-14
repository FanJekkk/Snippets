from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from MainApp.models import Snippet, Comment, User
from MainApp.forms import SnippetForm, UserRegistrationForm, CommentForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count, Sum
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from django.contrib import messages
from django.contrib.auth import get_user_model




def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)

@login_required(login_url='/accounts/login')
def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {'pagename': 'Добавление нового сниппета', 'form': form}
        return render(request, 'pages/add_snippet.html', context)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet=form.save()
            if request.user.is_anonymous:
                snippet.user = None
            else:
                snippet.user = request.user
            snippet.save()
            messages.success(request, 'Сниппет успешно добавлен!')
            return redirect("snippets")

def snippets_page(request):
    if request.user.is_anonymous:
        snippets = Snippet.objects.all().filter(parametr='Публичный')
    else:
        snippets = Snippet.objects.all().filter(Q(parametr='Публичный') | Q(user=request.user))
    if request.GET:
        sort = request.GET.get('sort')
        snippets = snippets.order_by(sort)
    users = get_user_model().objects.all()
    lang = Snippet.objects.values('lang').distinct()
    context = {'snippets': snippets, 'users': users, 'lang': lang}
    return render(request, 'pages/view_snippets.html', context)

def snippets_hidden(request):
    snippets = Snippet.objects.all().filter(parametr='Частный')
    users = get_user_model().objects.all()
    lang = Snippet.objects.values('lang').distinct()
    context = {'snippets': snippets, 'users': users, 'lang': lang}
    return render(request, 'pages/view_snippets.html', context)

def snippets_all(request):
    snippets = Snippet.objects.all()
    users = get_user_model().objects.all()
    lang = Snippet.objects.values('lang').distinct()
    context = {'snippets': snippets, 'users': users,'lang': lang}
    return render(request, 'pages/view_snippets.html', context)


def del_snippet_page(request, id):
    snippets = Snippet.objects.filter(id=id)
    snippets.delete()
    return redirect("snippets")

def snippet_detail(request, id):
    snippet = get_object_or_404(Snippet, id=id)
    code = 'print "Hello World"'
    print(highlight(code, PythonLexer(), HtmlFormatter()))
    form = CommentForm()
    context = {
        'pagename': 'Подробнее о сниппете',
        "snippet": snippet,
        "form": form
    }
    return render(request, 'pages/snippet_details.html', context)


def upd_snippet_page(request, id):
    form_data = request.POST
    name = form_data["name"]
    lang = form_data["lang"]
    code = form_data["code"]
    creation_date = form_data['creation_date']
    parametr = form_data['parametr']
    snippet = Snippet.objects.filter(id=id)
    snippet.update(name=name,lang=lang,code=code,creation_date=creation_date,parametr=parametr)
    return redirect("snippets")


def login_page(request):
    context={'page_name': 'Авторизация'}
    return render(request,'accounts/login.html', context)

def login(request):
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
        return render(request, 'accounts/registration.html', context)
    if request.method == "POST":  # информацию от формы
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        context = {'pagename': 'Регистрация пользователя', "form": form}
        return render(request, 'accounts/registration.html', context)

def my_snippets(request):
    snippets = Snippet.objects.all().filter(user=request.user)
    if request.GET:
        sort = request.GET.get('sort')
        snippets = snippets.order_by(sort)
    lang = Snippet.objects.values('lang').distinct()
    users = get_user_model().objects.all()
    context = {'snippets': snippets, 'users': users,'lang': lang}
    return render(request, 'pages/view_snippets.html', context)

def comment_add(request):
    if request.method == "POST":
        comment_form = CommentForm(request.POST, request.FILES)
        snippet_id = request.POST.get("snippet_id")
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.snippet = Snippet.objects.get(id=snippet_id)
            comment.save()

        return redirect(f'/snippet/{snippet_id}')

    raise Http404

def search_snippet(request):
    form_data = request.POST
    search_id = form_data["search_id"]
    if form_data["search_id"]:
        lang = Snippet.objects.values('lang').distinct()
        users = get_user_model().objects.all()
        snippets = Snippet.objects.all().filter(pk=search_id)
        if snippets.count() == 0:
            messages.warning(request, 'Не найдено данного сниппета!')
            context = {'pagename': 'PythonBin', 'error': 'Введите число'}
            return render(request, 'pages/index.html', context)
        else:
            context = {'snippets': snippets, 'users': users, 'lang': lang}
            return render(request, 'pages/view_snippets.html', context)


    else:
        messages.warning(request, 'Введите номер сниппета!')
        context = {'pagename': 'PythonBin', 'error':'Введите число'}
        return render(request, 'pages/index.html', context)

def filter_by_user(request,id):
    sort = request.GET.get('sort')
    if request.user.is_anonymous:
        snippets = Snippet.objects.all().filter(parametr='Публичный')
    else:
        snippets = Snippet.objects.all().filter(Q(parametr='Публичный') | Q(user=request.user))
    snippets = snippets.filter(user=id)
    if sort is not None:
        snippets = snippets.order_by(sort)
    lang = Snippet.objects.values('lang').distinct()
    users = get_user_model().objects.all()
    context = {'snippets': snippets, 'users': users,'lang': lang}
    return render(request, 'pages/view_snippets.html', context)

def filter_by_lang(request,lang):
    sort = request.GET.get('sort')
    if request.user.is_anonymous:
        snippets = Snippet.objects.all().filter(parametr='Публичный')
    else:
        snippets = Snippet.objects.all().filter(Q(parametr='Публичный') | Q(user=request.user))
    snippets = snippets.filter(lang=lang)
    if sort is not None:
        snippets = snippets.order_by(sort)
    lang = Snippet.objects.values('lang').distinct()
    users = get_user_model().objects.all()
    context = {'snippets': snippets, 'users': users,'lang': lang}
    return render(request, 'pages/view_snippets.html', context)

def rating_users(request):
    rating = Snippet.objects.all()
    snippets = Snippet.objects.all().count()
    comments = Comment.objects.all().count()
    rating = User.objects.raw("select au.id, au.username , count(distinct mas.id) as snippet , count(comment) as comment,"
                              " (count(distinct mas.id) + count(comment)) as rating from auth_user au "
                         " left join MainApp_snippet mas on mas.user_id = au.id"
                         " left join MainApp_comment mac ON mac.snippet_id = mas.id "
                         " group by au.id, au.username order by 3 desc;")
    context = {'pagename':'Рейтинг пользователей', 'users': rating, 'comments_count': comments, 'snippets_count': snippets}
    return render(request, 'pages/rating_users.html', context)
