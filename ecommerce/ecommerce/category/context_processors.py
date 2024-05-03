from .models import Category

def category_links(request):
    links = Category.objects.values('category_name', 'slug')
    return {'links': links}
