import json, requests, random, re
from pprint import pprint

from django.views import generic
from django.http.response import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

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
    # Facebook recommends going through every entry since they might send
    # multiple messages in a single call during high load
    for entry in incoming_message['entry']:
      for message in entry['messaging']:
        # Check to make sure the received call is a message call
        # This might be delivery, optin, postback for other events
        if 'message' in message:
          # Print the message to the terminal
          pprint(message)
            post_facebook_message(message['sender']['id'], message['message']['text'])
      return HttpResponse()

def post_facebook_message(fbid, recevied_message):
  post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAR79XI6ZBqUBAAUhLg2LChl0xI8j4lZC4fIOZAFic9O4Kl0xJYUnCJW81G5kcdZAVBPOepprGCn8Bm4WkRdHs3Pn52IqtDnIlsLq2LIDGro91sFo0Dlz7SsYWkFlvaSu0qnFSxgbnUI22QX8lIgJdZBvkRaM1EPtqgDegqPOIgZDZD'
  
  response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":recevied_message}})
  status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
  pprint(status.json())
