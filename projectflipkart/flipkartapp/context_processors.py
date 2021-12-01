from . models import cat
def menulink(request):
    links=cat.objects.all()
    return dict(links=links)