import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ivote.settings')
django.setup()

from .app.models import Party

parties = ["Likud","Blue&White","Emet","Shass","joint-list","Yemina",'Israel-beytenu','Ale-yarok']

for party in parties:
    p = Party(name=party)
    p.save()
print("done")