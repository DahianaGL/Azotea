from django.shortcuts import render
from Blog.models import Foto
# Create your views here.
def blog(request):
    fotos    = Foto.objects.all()
    return render(request, "blog/blog.html", {
        "fotos":    fotos
    })