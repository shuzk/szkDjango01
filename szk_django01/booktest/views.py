from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from booktest.models import BookInfo


# Create your views here.
#
# def index(request):
#     return HttpResponse("index")


# def index(request):
#     # 1.获取模板
#     template = loader.get_template("booktest/index.html")
#     # 2.定义上下文
#     context = RequestContext(request, {"title": "图书列表", "list": range(10)})
#     # 3.渲染模板
#     return HttpResponse(template.render(context))


# def index(request):
#     context = {"title": "图书列表", "list": range(10)}
#     return render(request, "booktest/index.html", context)


def index(request):
    # 查询所有图书
    booklist = BookInfo.objects.all()
    # 将图书列表传递到模板中，然后渲染模板
    return render(request, "booktest/index.html", {"booklist": booklist})


def detail(request, bid):
    # 根据图书编号对应图书
    book = BookInfo.objects.get(id=int(bid))
    # 查找book图书中的所有英雄信息
    heros = book.heroinfo_set.all()
    # 将图书信息传递到模板中，然后渲染模板
    return render(request, "booktest/detail.html", {"book": book, "heros": heros})
