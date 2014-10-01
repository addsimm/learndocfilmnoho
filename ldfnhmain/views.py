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
        discussdoc = DiscussDoc(parent=discussdocs_key())  # finicky about order of args in get or insert

        if users.get_current_user():
            discussdoc.dd_adder = users.get_current_user()

        discussdoc.dd_url = request.POST.get('url')
        if request.POST.get('title'):
            discussdoc.dd_title = request.POST.get('title')
        else:
            discussdoc.dd_title = discussdoc.dd_url
        discussdoc.put()
        return redirect('home')

    path = request.get_full_path()
    page_name = 'Home'
    view = path + page_name.lower()
    discuss_docs_query = DiscussDoc.query(ancestor=discussdocs_key())
    discussed_docs = discuss_docs_query.filter(DiscussDoc.dd_discussed == True).fetch(30)
    current_docs = discuss_docs_query.filter(DiscussDoc.dd_discussed == False).fetch(30)

    template_values = return_template_values(path)
    template_values.update(csrf(request))
    template_values.update({'page_name': page_name,
                            'view': view,
                            'discussedDocs': discussed_docs,
                            'currentDocs': current_docs
                            })

    return render_to_response('home.html', template_values)

