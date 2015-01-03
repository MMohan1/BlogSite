from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from blogs.models import Blog, Action


def index(request):
    if request.POST == {}:
        latest_blog_list = Blog.objects.order_by('-pub_date')[:5]
        context = {'latest_blog_list': latest_blog_list}
        return render(request, 'blogs/index.html', context)
    else:
        try:
            if (request.POST['url'] == u' ' or request.POST['description'] == u'' or request.POST['value'] == u' ' or request.POST['url'] == u' ' or request.POST['blog_title'] == u' ' or request.POST['date'] == u' '):
                raise Exception("Enter value")
            else:
                action_obj = Blog(Blog_Title=request.POST['blog_title'], Blog_Field=request.POST[
                    'value'], URL=request.POST['url'], Blog_Description=request.POST['description'], pub_date=request.POST['date'])
        except Exception:
            return render(request, 'blogs/addblock.html', {'error_message': "Please Enter Full Information."})
        else:
            action_obj.save()
            return HttpResponseRedirect(reverse('blogs:index'))


def addblock(request):
    return render(request, 'blogs/addblock.html')


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/details.html', {'blog': blog})
    # return HttpResponse("You're looking at blog %s." % blog_id)


def results(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/results.html', {'blog': blog})


def addblog(request):
    #blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/index.html')


def vote(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    try:
        if (request.POST['user_name'] == u' ' or request.POST['comment'] == u''):
            raise Exception("Enter value")
        else:
            action_obj = Action(Blog_Title=blog, User_Name=request.POST[
                'user_name'], Comment=request.POST['comment'])
    except Exception:
        # Redisplay the question voting form.
        return render(request, 'blogs/details.html', {
            'blog': blog,
            'error_message': "Please comment and write user name.",
        })
    else:
        #selected_choice.votes += 1
        action_obj.save()
        # comment.save()
        # Always return an HttpResponseRedirect after successfully dealing
        return HttpResponseRedirect(reverse('blogs:results', args=(blog.id,)))
