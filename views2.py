import json, requests, random, re
import textrazor
from pprint import pprint

from django.views import generic
from django.http.response import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from sentiment import Helper
from postFacebook import Facebook


# Create your views here.
textrazor.api_key = "8e7917d3aac5284a31d60d6797bdea981c38ead610eb5ab2fcb9ed5b"
# Create your views here.
class Start(generic.View):
  
  def get(self, request, *args, **kwargs):
    if request.method == "GET":
      if self.request.GET['hub.verify_token'] == '1218':
        return HttpResponse(self.request.GET['hub.challenge'])
        else:
          return HttpResponse("Invalid token")


@method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return generic.View.dispatch(self, request, *args, **kwargs)
  
  # Post function to handle Facebook messages
  def post(self, request, *args, **kwargs):
    # Converts the text payload into a python dictionary
    incoming_message = json.loads(self.request.body.decode('utf-8'))
    print("\n\n\n-----------------------------JSON---------------\n\n\n")
    print(incoming_message)
    print("\n\n\n-----------------------------JSON---------------\n\n\n")
    id = incoming_message['entry'][0]['messaging'][0]['sender']['id']
    if 'postback' in incoming_message['entry'][0]['messaging'][0]:
      payload = incoming_message['entry'][0]['messaging'][0]['postback']['payload']
      if payload == "Startup":
        Facebook.post_facebook_message(str(id), 'startup')
        Facebook.post_facebook_message(str(id),'load')
        Facebook.post_facebook_message(str(id), 'startup2')
        Facebook.post_facebook_message(str(id),'load')
        Facebook.post_facebook_message(str(id),'load')
        Facebook.post_facebook_message(str(id), 'startup3')
        return HttpResponse(200)
      if payload == "Happy":
        Facebook.post_facebook_message(str(id),'load')
        Facebook.post_facebook_message(str(id),'load')
        Facebook.post_facebook_message(str(id),'message')
        Facebook.post_facebook_message(str(id),'happy')
        return HttpResponse(200)
      if payload == "Sad":
        Facebook.post_facebook_message(str(id),'load')
        Facebook.post_facebook_message(str(id),'load')
        Facebook.post_facebook_message(str(id),'message')
        Facebook.post_facebook_message(str(id), 'sad')
        return HttpResponse(200)
      if payload == "Cute":
        Facebook.post_facebook_message(str(id),'load')
        Facebook.post_facebook_message(str(id),'load')
        Facebook.post_facebook_message(str(id),'message')
        Facebook.post_facebook_message(str(id), 'cute')
        return HttpResponse(200)
      if payload == "General":
        Facebook.post_facebook_message(str(id),'load')
        Facebook.post_facebook_message(str(id), 'general')
        return HttpResponse(200)
      if payload == "Emotions":
        Facebook.post_facebook_message(str(id),'load')
        Facebook.post_facebook_message(str(id), 'emotions')
        return HttpResponse(200)
      if payload == "Write":
        Facebook.post_facebook_message(str(id),'load')
        Facebook.post_facebook_message(str(id), 'write')
        return HttpResponse(200)
      if payload == "Guide":
        Facebook.post_facebook_message(str(id),'load')
        Facebook.post_facebook_message(str(id), 'guide')
        return HttpResponse(200)
      if payload == "Options":
        Facebook.post_facebook_message(str(id),'load')
        Facebook.post_facebook_message(str(id),'load')
        Facebook.post_facebook_message(str(id), 'startup3')
        return HttpResponse(200)
    
    
    
    
    
    
    
    
    
    
    
    #    if 'postback' in incoming_message['entry'][0]['messaging'][0]:
    #      id = incoming_message['entry'][0]['messaging'][0]['sender']['id']
    #      post_facebook_message(str(id), 'startup')
    #      post_facebook_message(str(id),'load')
    #      post_facebook_message(str(id), 'startup2')
    #      post_facebook_message(str(id),'load')
    #      post_facebook_message(str(id), 'startup3')
    #      return HttpResponse(200)
    
    # Facebook recommends going through every entry since they might send
    # multiple messages in a single call during high load
    for entry in incoming_message['entry']:
      #pprint(entry)
      for message in entry['messaging']:
        # Check to make sure the received call is a message call
        # This might be delivery, optin, postback for other events
        if 'message' in message:
          # Print the message to the terminal
          if 'text' not in message['message']:
            continue
            else:
              input = message['message']['text']
              print(input)
              if len(input) >= 25:
                #TODO SENTIMENT ANALYSIS + FILE BUILDING
                val = Helper.sentimentHelper(input)
                if val == "positive":
                  Facebook.post_facebook_message(str(id),'load')
                  Facebook.post_facebook_message(id,'message2')
                  Facebook.post_facebook_message(str(id),'load')
                  Facebook.post_facebook_message(str(id),'load')
                  Facebook.post_facebook_message(id,val)
                  return HttpResponse(200)
                if val == "negative":
                  Facebook.post_facebook_message(str(id),'load')
                  Facebook.post_facebook_message(id,'message3')
                  Facebook.post_facebook_message(str(id),'load')
                  Facebook.post_facebook_message(str(id),'load')
                  Facebook.post_facebook_message(id,val)
                  return HttpResponse(200)
                if val == "neutral":
                  Facebook.post_facebook_message(str(id),'load')
                  Facebook.post_facebook_message(id,val)
                  return HttpResponse(200)
              # post_facebook_message(str(message['sender']['id']), )
              Facebook.post_facebook_message(str(id),'load')
              Facebook.post_facebook_message(str(message['sender']['id']),input)
    return HttpResponse(200)
