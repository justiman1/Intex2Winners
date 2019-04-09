from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from drug import models as dmod

@view_function
def process_request(request):
    
    instance = []
    
    for item in dmod.Opioids.objects.all():
        instance.append(item)

    context = {
        'instance': instance,
    }
    return request.dmp.render('index.html', context)


