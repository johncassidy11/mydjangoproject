# Create your views here.
from django.template.loader import get_template
from django.template.loader import Context
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
import datetime


def hello(request):
    return HttpResponse('welcome to %s' % request.path_info)


def display(request):
    #ua = request.META.get('HTTP_USER_AGENT','unknown')
    #return HttpResponse('Your browser is %s' % ua)
    values = request.META.items()
    values.sort()
    html = []
    k = {k for k in values}
    v = {v for v in values}
    print k

    #    html.append('<tr><td>%s</td><td>%s</td></tr>' %(k, v))
    #return HttpResponse('<table>%s</table>' % (html))

    return render_to_response('dateapp/meta.html', {'values': values}


    )


def current_time(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


def current_time(request):
    current_date = datetime.datetime.now()

    return render_to_response('dateapp/current_datetime.html', {'current_date': current_date})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>cherez %s chasov budet %s<body></html>" % (offset, dt)
    return HttpResponse(html)
		