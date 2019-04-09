from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from drug import models as dmod

@view_function
def process_request(request, drug):
    prescribers = []
    instance = []
    
    for item in dmod.Opioids.objects.all():
        instance.append(item)

    context = {
        'instance': instance,
    }

    for dr in dmod.PrescriberInfo.objects.raw('SELECT TOP(10) DoctorID, fname, lname, ' + drug + ' AS quantity FROM prescriber_info ORDER BY ' + drug + ' DESC'):
        prescribers.append(dr)
    
    context = {
        'instance': instance,
        'drug': drug,
        'prescribers': prescribers,
    }

    return request.dmp.render('top10.html', context)