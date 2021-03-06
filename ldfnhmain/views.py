# Create your views here.

import datetime
from socket import gethostname

from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from google.appengine.api import users

from ldfnh.models import *


def return_template_values(path):
    if users.get_current_user():
        url = users.create_logout_url(path)
        url_linktext = 'sign out'
        template_values = {'user': users.get_current_user().nickname()}
    else:
        url = users.create_login_url(path)
        url_linktext = 'sign in'
        template_values = {}

    now = datetime.datetime.now()
    host = gethostname()
    template_values.update({'url': url,
                            'url_linktext': url_linktext,
                            'now': now,
                            'host': host,
                            'path': path
                            })

    return template_values


def home(request):
    if request.method == 'POST':
        doc927 = Doc927(parent=doc927s_key())  # finicky about order of args in get or insert

        if users.get_current_user():
            doc927.d927_adder = users.get_current_user()

        doc927.d927_url = request.POST.get('url')
        doc927.put()
        return redirect('home')

    path = request.get_full_path()
    page_name = 'Home'
    view = path + page_name.lower()
    doc927s_query = Doc927.query(ancestor=doc927s_key())
    doc927s = doc927s_query.fetch(30)

    template_values = return_template_values(path)
    template_values.update(csrf(request))
    template_values.update({'page_name': page_name,
                            'view': view,
                            'doc927s': doc927s,
                            })

    return render_to_response('home.html', template_values)


from google.appengine.ext.webapp import blobstore_handlers


class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        upload_files = self.get_uploads('file')  # 'file' is file upload field in the form
        blob_info = upload_files[0]
        self.redirect('/serve/%s' % blob_info.key())