from pyramid.view import view_config
from pyramid.httpexceptions import HTTPUnauthorized, HTTPNotFound, HTTPFound
from pyramid.response import Response

import os, glob, time


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home(request):
    return {} # no parameters for the jinja renderer

@view_config(route_name='async_get', renderer='../templates/async_get.jinja2')
def async_get(request):
    return {} # no parameters for the jinja renderer

@view_config(route_name='async_get2')
def async_get2(request):
    # access GET parameters like this:
    first_name = request.params.get("first_name", "nadie")
    last_name = request.params.get("last_name", "nadie")
    print(first_name, last_name)
    # list main dir
    # files = glob.glob(os.path.join(os.path.expanduser("~"),"*"))
    files = glob.glob("/usr/sbin/ch*")
    # & some artificial lag:
    time.sleep(3)
    return Response(
        json = {
            "error": "",
            "files": files
            }
    )

@view_config(route_name='download', renderer='../templates/download.jinja2')
def download(request):
    return {} # no parameters for the jinja renderer

@view_config(route_name='download2')
def download2(request):
    # files = glob.glob(os.path.join(os.path.expanduser("~"),"*"))
    files = glob.glob("/usr/sbin/ch*")
    fullpath = files[0]
    filename = fullpath.split("/")[-1]
    f = open(fullpath, "rb")
    return Response(
        body_file = f,
        content_disposition = 'attachment; filename=%s' % filename,
        content_type = 'application/octet-stream'
        )
