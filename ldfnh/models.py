# Create your models here.

from google.appengine.ext import ndb


def doc927s_key():
    """Constructs a Datastore key for the Doc927s entity named doc927s."""
    return ndb.Key('Doc927s', 'doc927s')


class Doc927(ndb.Model):
    d927_adder = ndb.UserProperty()
    d927_url = ndb.StringProperty()
    d927_date_created = ndb.DateTimeProperty(auto_now_add=True)


