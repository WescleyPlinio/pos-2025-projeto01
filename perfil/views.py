from django.shortcuts import render, redirect
from django.urls import reverse
from .oauth import oauth

def index(request):
    return render(request, 'index.html')

def auth(request):
    token = oauth.suap.authorize_access_token()
    request.session['suap_token'] = token
    return redirect(index)

def login(request):
    redirect_uri = request.build_absolute_uri(reverse(auth(request)))
    return oauth.suap.authorize_redirect(request, redirect_uri)
