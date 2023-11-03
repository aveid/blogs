from django.shortcuts import render


# Create your views here.
from blog.models import Blog


def get_main_page(request):
    news = Blog.objects.all()
    return render(request, "blog/main_page.html", locals())

def get_detail_blog(request, pk):
    new = Blog.objects.get(id=pk)
    return render(request, "blog/detail_page.html", locals())

