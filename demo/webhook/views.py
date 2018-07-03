# PYTHON wеbhooks code example by ClassMarker.com

import json
import hmac
import hashlib
import base64
import os
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

def verify_payload(payload, header_hmac_signature):

    webhook_secret = 'YOUR_CLASSMARKER_WEBHOOK_SECRET_PHRASE'
    dig = hmac.new(webhook_secret.encode(), msg=payload, digestmod=hashlib.sha256).digest()
    calculated_signature = base64.b64encode(dig).decode().encode('ascii','ignore')

    # X_CLASSMARKER_HMAC_SHA256 header may looks like "ASd=,ASd="
    if ',' in header_hmac_signature:
        header_hmac_signature = header_hmac_signature.split(',')[0]

    return hmac.compare_digest(calculated_signature, header_hmac_signature)

@csrf_exempt
def webhook_view(request):
    print("received webhook request")

    hmac_header = request.META.get('HTTP_X_CLASSMARKER_HMAC_SHA256')

    if verify_payload(request.body, hmac_header):
        # Save results in your database.
        # Important: Do not use a script that will take a long time to respond.
        print("200")
        return HttpResponse("OK", status=200)
    else:
        print("400")
        return HttpResponse("Fail", status=400)
