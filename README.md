# TokenAuthentication

> pip install ipython

> pip install djangorestframework

> mkdir files

> python manage.py startapp accounts
> python manage.py startapp polls

[edit /TokenAuthentication/settings.py](https://github.com/mingburnu/TokenAuthentication/blob/master/TokenAuthentication/settings.py)

    TEMPLATES = [
        {
            ...
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            ...
        },
    ]

    INSTALLED_APPS = [
        ...
		'polls',
		'accounts',
		'rest_framework',
		'rest_framework.authtoken',
    ]
    
    STATIC_URL = '/static/'
    
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
    
    STATIC_ROOT = os.path.join(BASE_DIR, 'files')
    
    LOGIN_URL = '/'
        
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        )
    }

[edit /TokenAuthentication/accounts/models.py](https://github.com/mingburnu/TokenAuthentication/blob/master/accounts/models.py)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


[edit /TokenAuthentication/polls/models.py](https://github.com/mingburnu/TokenAuthentication/blob/master/polls/models.py)

    class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')
    
        def __unicode__(self):
            return self.question_text
    
    
    class Choice(models.Model):
        question = models.ForeignKey(Question, related_name="choices")
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)
    
        def __unicode__(self):
            return self.choice_text

[edit TokenAuthentication/polls/serializer.py](https://github.com/mingburnu/TokenAuthentication/blob/master/polls/serializers.py)

[edit /TokenAuthentication/polls/admin.py](https://github.com/mingburnu/TokenAuthentication/blob/master/polls/admin.py)
   
    admin.site.register(polls)
    admin.site.register(accounts)
	
> python manage.py makemigrations<br>
> python manage.py migrate<br>

> python manage.py createsuperuser

> from django.contrib.auth.models import User from
> rest_framework.authtoken.models import Token
> 
> users = User.objects.all() for user in users:
>     token, created = Token.objects.get_or_create(user=user)
>     print(user.username, token.key)

[edit TokenAuthentication/polls/views.py](https://github.com/mingburnu/TokenAuthentication/blob/master/polls/views.py)

[edit TokenAuthentication/accounts/views.py](https://github.com/mingburnu/TokenAuthentication/blob/master/accounts/views.py)

[edit TokenAuthentication/polls/urls.py](https://github.com/mingburnu/TokenAuthentication/blob/master/polls/urls.py)

[edit TokenAuthentication/accounts/urls.py](https://github.com/mingburnu/TokenAuthentication/blob/master/accounts/urls.py)

[edit TokenAuthentication/urls.py](https://github.com/mingburnu/TokenAuthentication/blob/master/TokenAuthentication/urls.py)

[127.0.0.1:8000](http://127.0.0.1:8000)

### REFERECE
[How to Implement Token Authentication with Django REST Framework](https://chrisbartos.com/articles/how-to-implement-token-authentication-with-django-rest-framework/)
[用戶的登入與登出](http://dokelung-blog.logdown.com/posts/222552-django-notes-9-cookies-and-sessions)
