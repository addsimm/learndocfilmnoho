# Create your models here.

from google.appengine.ext import ndb


def discussdocs_key():
    """Constructs a Datastore key for the DiscussionDocs entity named DiscussionDocs."""
    return ndb.Key('DiscussDocs', 'DiscussDocs')


class DiscussDoc(ndb.Model):
    dd_adder = ndb.UserProperty()
    dd_url = ndb.StringProperty()
    dd_title = ndb.StringProperty(default=dd_url)
    dd_date_created = ndb.DateTimeProperty(auto_now_add=True)
    dd_discussed = ndb.BooleanProperty(default=False)


