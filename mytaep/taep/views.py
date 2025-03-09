from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'taep/index.html')

def about(request):
    return render(request, 'taep/about.html')

def contact(request):
    return render(request, 'taep/contact.html')

def services(request):
    return render(request, 'taep/services.html')

def blog(request):
    return render(request, 'taep/blog.html')

def testimonial(request):
    return render(request, 'taep/testimonial.html')
