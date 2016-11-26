import json, requests, random, re
import textrazor
from pprint import pprint

from django.views import generic
from django.http.response import HttpResponse


class Helper:
  
  @staticmethod
  def sentimentHelper(entry):
    response = requests.post('http://sentiment.vivekn.com/api/batch/',headers={"Content-Type": "application/json"},data=json.dumps([entry]))
    return response.json()



