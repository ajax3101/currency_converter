from multiprocessing import context
from django.shortcuts import render

def exchange (request):
    name = 'Denys'

    context = {
        'name':name
    }
    return render(request=request, template_name='exchange_app/base.html', content=context)