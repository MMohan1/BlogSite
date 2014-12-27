from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from blogs.models import Blog, Action


def index(request):
    latest_blog_list = Blog.objects.order_by('-pub_date')[:5]
    context = {'latest_blog_list': latest_blog_list}
    return render(request, 'blogs/index.html', context)

    """latest_blog_list = Blog.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.Blog_Title for p in latest_blog_list])
    return HttpResponse(output)"""


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/details.html', {'blog': blog})
    # return HttpResponse("You're looking at blog %s." % blog_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
