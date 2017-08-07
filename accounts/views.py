from django.conf import settings
from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token


def login_user(request):
    if request.user.is_authenticated() and request.COOKIES.get('token') == request.session['auth']:
        return HttpResponseRedirect(settings.LOGIN_URL)
    else:
        auth.logout(request)

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        # the password verified for the user
        if user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            request.session['auth'] = token.key
            auth.login(request, user)
            return redirect(settings.LOGIN_URL, request)

    return redirect(settings.LOGIN_URL, request)


def logout_user(request):
    auth.logout(request)
    return redirect(settings.LOGIN_URL, request)
