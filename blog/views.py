from django.shortcuts import render


# Create your views here.
from blog.models import Blog


def get_main_page(request):
    news = Blog.objects.all()
    return render(request, "blog/main_page.html", locals())
