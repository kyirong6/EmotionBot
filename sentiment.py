import json, requests, random, re
from pprint import pprint

from django.views import generic
from django.http.response import HttpResponse


class Helper:
  
  @staticmethod
  def sentimentHelper(entry):
    api_key = "85149fdbc99541b9fc7dd83cc6ee18c4iEYFx-1ADGR_ZO9fIdoQanCt3MqbHTXe"
    url ="https://api.sentigem.com/external/get-sentiment?api-key={a}&text={b}".format(a=api_key,b=entry)
    response = requests.get(url)
    value = response.json()['polarity']
    return value


