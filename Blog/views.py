from django.shortcuts import render
from django.core.paginator import Paginator
from Blog.models import Foto
# Create your views here.
def blog(request):
    fotos = Foto.objects.all()

    #paginacion
    paginator = Paginator(fotos, 9)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, "blog/blog.html", {
        "fotos": page_obj,
        "page_obj": page_obj,
    })