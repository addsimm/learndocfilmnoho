# Create your models here.

from google.appengine.ext import ndb


def flatpages_key():
    """Constructs a Datastore key for the Flatpages entity named pages."""
    return ndb.Key('Flatpages', 'pages')


class Flatpage(ndb.Model):
    fp_author = ndb.StringProperty()
    fp_content = ndb.TextProperty()
    fp_date_created = ndb.DateTimeProperty(auto_now_add=True)


