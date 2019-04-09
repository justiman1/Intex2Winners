from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from drug import models as dmod

@view_function
def process_request(request, doctor):
    dr = dmod.PrescriberInfo.objects.get(doctorid = doctor)

    medications = []
    for m in dmod.Triple.objects.filter(doctorid = dr.doctorid):
        medications.append(m)

    context = {
        'dr': dr,
        'medications': medications,
    }
    return request.dmp.render('index.html', context)