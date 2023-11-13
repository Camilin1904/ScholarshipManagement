
from django.http import HttpResponse


def Icesi(request):
    img = open('./ScholarshipModule/static/Icons/si.png', 'rb')
    return HttpResponse(img, content_type="image/png")
