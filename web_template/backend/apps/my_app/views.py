from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')

def about(request):
    return render(request, 'my_app/about.html')

def gallery(request):
    return render(request, 'my_app/gallery.html')

def data(request):
    return render(request, 'my_app/data.html')

def papers(request):
    return render(request, 'my_app/papers.html')
