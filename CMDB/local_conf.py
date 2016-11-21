import mongoengine

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
    }
}

#ENGINE = 'mongoengine.django.auth.MongoEngineBackend'
SESSION_ENGINE = 'django_mongoengine.sessions'
SESSION_SERIALIZER = 'django_mongoengine.sessions.BSONSerializer'

_MONGODB_USER = 'mongotest'
_MONGODB_PASSWD = 'mongotest'
_MONGODB_HOST = '127.0.0.1'
_MONGODB_NAME = 'mongotest'
_MONGODB_DATABASE_HOST = \
    'mongodb://%s:%s@%s/%s' \
    % (_MONGODB_USER, _MONGODB_PASSWD, _MONGODB_HOST, _MONGODB_NAME)

MONGODB_DATABASES = {
    "default": {
        "name": _MONGODB_NAME,
        "host": _MONGODB_HOST,
        "password": _MONGODB_PASSWD,
        "username": _MONGODB_USER,
        "tz_aware": True, # if you using timezones in django (USE_TZ = True)
    },
}

AUTHENTICATION_BACKENDS = (
    'django_mongoengine.mongo_auth.backends.MongoEngineBackend',
)
AUTH_USER_MODEL = 'mongo_auth.MongoUser'