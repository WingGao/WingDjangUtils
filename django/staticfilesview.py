from django.contrib.staticfiles import views as sfview


# url(r'^static/(?P<path>.*)$', sfview.serve),

def serve(request, path):
    return sfview.serve(request, path, True)
