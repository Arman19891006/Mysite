from django.shortcuts import render

# Create your views here.
def blog_view(request):
    return render(request, 'blog/blog-home.html')


def blog_single(request):
    context = {'title': 'sdsfasdas','content' : 'saaaaaaaaaaaaaaaaaasadsadsadsadsa'}
    return render(request, 'blog/blog-single.html',context)

