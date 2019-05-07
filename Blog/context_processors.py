from .models import Blurb

def BlurbContext(request):
    blurb = Blurb.objects.all().first()

    if blurb is not None:
        return {'blurb': blurb}
    else:
        return {'blurb': 'Add a blurb'}
