

from django.shortcuts import render
from django.template import RequestContext

def index(request):
        ctxt = {}
        return render(request, 'upload.html', ctxt)