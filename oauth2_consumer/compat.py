import random

try:
    random = random.SystemRandom()
except NotImplementedError:
    pass

def get_random_string(length=12, allowed_chars='abcdefghijklmnopqrstuvwxyz'
                                               'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                                               '0123456789'):
    return ''.join([random.choice(allowed_chars) for i in range(length)])

def get_user_model():
    try:
        from django.contrib.auth import get_user_model
        
        return get_user_model()
    except ImportError:
        from django.contrib.auth.models import User
        
        return User
