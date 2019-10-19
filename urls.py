from django.contrib import admin
from django.urls import path
from django.conf.urls import url
import phototo.views
urlpatterns = [
    url('signin/', phototo.views.signin.index),
    url('signout/', phototo.views.signout.index),
    url('uploadDo/', phototo.views.uploadDo.index),
    url('upload/', phototo.views.upload.index),
    url('userMailConfirmation/', phototo.views.userMailConfirmation.index),
    url('userSignUpDo/', phototo.views.userSignUpDo.index),
    url('userSignUp/', phototo.views.userSignUp.index),
    url('', phototo.views.top.index),
]
