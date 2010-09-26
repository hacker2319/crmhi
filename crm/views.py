# -*- coding: utf-8 -*-
from os import path
from crm.models import *
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper

def createQuotePDF(request, quoteid):
   quote = Quote.objects.get(id=quoteid)
   pdf = quote.createPDF(purchaseconfirmation=False)
   response = HttpResponse(FileWrapper(file(pdf)), mimetype='application/pdf')
   response['Content-Length'] = path.getsize(pdf)
   return response