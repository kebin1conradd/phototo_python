from django.http import HttpResponse
from ..models.dataBaseMapper.photos  import modelPhotos
from ..models.login.auth import modelLoginAuth
from ..models.common import modelCommon
from django.conf import settings
from django.shortcuts import render

import pprint

def index(request):
    
    photo_list = modelPhotos.objects.order_by('-add_date')[:3]
    top_photo_list = list()
    for top_photo in photo_list:
        top_photo.img_url = 'http://'+settings.S3_DOMAIN+'/phototo/pc/'+str(top_photo.photo_id) +'.' +top_photo.extension_name
        top_photo_list.append(top_photo)
    

    ctxt = {
        'top_photo_list':top_photo_list,
    }
    
    return render(request, 'top.html', ctxt)