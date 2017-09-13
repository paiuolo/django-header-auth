import uuid, hashlib
from django.utils import timezone
from django.conf import settings


def create_uuid():
    return str(uuid.uuid4())# .replace('-','')

def create_secret():
    now = str(timezone.now())
    chiave = "{}{}{}".format(now, settings.SECRET_KEY, create_uuid()).encode('utf-8')
    return hashlib.sha224(chiave).hexdigest()

def domain_email_extract(username):
    if username:
        tokens = str.split(username, "@")
        if len(tokens) == 3:
            return (tokens[2], "@".join([tokens[0], tokens[1]]))
    return ('example.com', 'anonymous@example.com')

def extract_groups(groups):
    if groups and groups != "":
        return list(map(str.strip, groups.split(',')))
    return []
