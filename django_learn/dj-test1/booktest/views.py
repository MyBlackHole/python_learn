from booktest.models import BookInfo
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext


# Create your views here.
def my_render(request, template_path, context_dict={}):
    temp = loader.get_template(template_path)

    context = RequestContext(request, context_dict)

    res_html = temp.render(context)

    return HttpResponse(res_html)


def index(request):
    return render(request, 'booktest/index.html', {'content': 'hello woeld', 'list': list(range(1, 10))})


def index2(request):
    return HttpResponse('hello python')


def show_books(request):
    books = BookInfo.objects.all()

    return render(request, 'booktest/show_books.html', {'book': books})


def detail(requst, bid):
    book = BookInfo.objects.get(id=bid)

    heros = book.heroinfo_set.all()

    return render(requst, 'booktest/detail.html', {'book': book, 'heros': heros})
