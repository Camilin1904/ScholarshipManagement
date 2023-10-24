import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django import template
import base64
import requests

#must install:
#pip install xhtml2pdf

def link_callback(uri, rel):
   """
   Convert HTML URIs to absolute system paths so xhtml2pdf can access those
   resources
   """
   import os
   from django.conf import settings

   static_url = settings.STATIC_URL       # Typically /static/
   static_root = settings.STATIC_ROOT     # Typically /home/userX/project_static/
   media_url = settings.MEDIA_URL         # Typically /media/
   media_root = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/
   base_dir = settings.BASE_DIR           # Project's base directory
   print("kkkkkkk", uri)
   print(static_root)
   print(static_url)
   if uri.startswith(media_url):
      path = os.path.join(media_root, uri.replace(media_url, ""))
   elif uri.startswith(static_url):
      print("pito")
      path = os.path.join(static_root, uri.replace(static_url, ""))
   else:
      return os.path.join(base_dir, '../', uri)
   
   print("aaaaa", path)
   
   print( os.path.isfile(path))

   # make sure that file exists
   if not os.path.isfile(path):
      raise Exception(
         'media URI must start with %s or %s' % (static_url, media_url)
      )
   return path

def render_pdf_view(request):
    template_path = 'HTML/reportTemplate.html'
    static_url = settings.STATIC_URL 
    print("ofjhsgdiu", static_url)
    context = {'img': to_base64(settings.STATIC_ROOT + "/Icons/icesi.png")}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
 
def to_base64(url):
   return "data:image/png;base64, " + str(base64.b64encode(requests.get(url).content))