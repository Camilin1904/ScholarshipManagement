import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from datetime import date
from ScholarshipModule.models import AnnouncementEvent


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

   if uri.startswith(media_url):
      path = os.path.join(media_root, uri.replace(media_url, ""))
   elif uri.startswith(static_url):
      path = os.path.join(static_root, uri.replace(static_url, ""))
   else:
      return os.path.join(base_dir, '../', uri)

   # make sure that file exists
   if not os.path.isfile(path):
      raise Exception(
         'media URI must start with %s or %s' % (static_url, media_url)
      )
   return path

def render_pdf_view(request):
   #Get the require announcement
   try:
      print("pito")
      announcementNum = request.session.get('announcementId')
      print(announcementNum)
      announcement = AnnouncementEvent.objects.filter(announcementId_id = announcementNum)
      context = {'date':date.today(), 'announcement': announcement}
   except:
      context = {'date':date.today(), 'error':'La convocatoria pedida no existe.'}
      
      
   template_path = 'HTML/reportTemplate.html'
   static_url = settings.STATIC_URL 
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
 
