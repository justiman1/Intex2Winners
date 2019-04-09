from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from drug import models as dmod

@view_function
def process_request(request, drugs:str):
    print(drugs)
    meds = dmod.Opioids.objects.get(drugname = drugs)

    prescribers = []
    for dr in dmod.PrescriberInfo.objects.raw('SELECT TOP(10) DoctorID, fname, lname, ' + drugs + ' AS quantity FROM prescriber_info ORDER BY ' + drugs + ' DESC'):
        prescribers.append(dr)
    
    context = {
        'meds': meds,
        'prescribers': prescribers,
    }

    return request.dmp.render('index.html', context)


