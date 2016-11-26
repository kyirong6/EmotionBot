import json, requests, random, re
import textrazor
from pprint import pprint

from django.views import generic
from django.http.response import HttpResponse


class Helper:
  
  @staticmethod
  def sentimentHelper(self, Entry):
    print("helper")
    return -1
