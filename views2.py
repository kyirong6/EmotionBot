import json, requests, random, re
import textrazor
from pprint import pprint

from django.views import generic
from django.http.response import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

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
    #print(incoming_message)
    if 'postback' in incoming_message['entry'][0]['messaging'][0]:
      id = incoming_message['entry'][0]['messaging'][0]['sender']['id']
      post_facebook_message(id, 'startup')
      post_facebook_message(id,'load')
      post_facebook_message(id, 'startup2')
      post_facebook_message(id,'load')
      post_facebook_message(id, 'startup3')
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
              print("------------------- I AM A SPLITTER {a}".format(a=1))
              post_facebook_message(message['sender']['id'], message['message']['text'])
    return HttpResponse()

def post_facebook_message(fbid, recevied_message):
  client = textrazor.TextRazor(extractors=["entities", "topics"])
  response = client.analyze("I am really sad right now".decode('utf-8'))
  #print(response.entities())
  
  for entity in response.entities():
    print(entity)
  post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAR79XI6ZBqUBAAUhLg2LChl0xI8j4lZC4fIOZAFic9O4Kl0xJYUnCJW81G5kcdZAVBPOepprGCn8Bm4WkRdHs3Pn52IqtDnIlsLq2LIDGro91sFo0Dlz7SsYWkFlvaSu0qnFSxgbnUI22QX8lIgJdZBvkRaM1EPtqgDegqPOIgZDZD'
  url = "https://petersapparel.parseapp.com"


  responses = {'load': {
    "recipient":{
      "id":fbid
    },
      "sender_action":"typing_on"
  },
    'startup': {"recipient":{"id":fbid}, "message":{"text": "Hey Choenden! Welcome to my platform. I can help you in a variety of ways depending on your mood and can even log some journals for you. :)"}} ,
      'startup2':{"recipient":{"id":fbid}, "message":{"text": "Please choose from the options below or enter 'Help'."}}  ,
        'startup3': {
          "recipient":{
            "id":fbid
},
  "message":{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"generic",
        "elements":[
                    {
                    "title":"Settings",
                    "subtitle":"Options",
                    "buttons":[
                               {
                               "type":"postback",
                               "payload":"DEVELOPER_DEFINED_PAYLOAD",
                               "title":"Option1"
                               },
                               {
                               "type":"postback",
                               "title":"Option2",
                               "payload":"DEVELOPER_DEFINED_PAYLOAD"
                               },
                               {
                               "type":"postback",
                               "title":"Option3",
                               "payload":"DEVELOPER_DEFINED_PAYLOAD"
                               }
                               
                               ]
                    }
                    ]
  }
}
}
},
  'happy': {"recipient":{"id":fbid}, "message":{"text": "You are happy"}},
    'sad': {"recipient":{"id":fbid}, "message":{"text": "You are sad"}},
      'help': {
        "recipient":{
          "id":fbid
          },
            "message":{
              "attachment":{
                "type":"template",
                "payload":{
                  "template_type":"button",
                  "text":"Here are some of my features",
                  "buttons":[
                             {
                             "type":"web_url",
                             "url":"https://petersapparel.parseapp.com",
                             "title":"Show Website"
                             },
                             {
                             "type":"postback",
                             "title":"Start Chatting",
                             "payload":"USER_DEFINED_PAYLOAD"
                             }
                             ]
            }
        }
          }
          },
            'movies':{
"recipient":{
  "id":fbid
  }, "message": {
    "attachment": {
      "type": "template",
        "payload": {
          "template_type": "list",
            "elements": [
                         {
                         "title": "Movies for you",
                         "image_url": "https://images.tenplay.com.au/~/media/TV%20Shows/Movies%20Hub/Movies_Logo_500x281.jpg",
                         "subtitle": "Choose the one for you",
                         "default_action": {
                         "type": "web_url",
                         "url": url,
                         "messenger_extensions": True,
                         "webview_height_ratio": "tall",
                         "fallback_url": url
                         },
                         "buttons": [
                                     {
                                     "title": "View",
                                     "type": "web_url",
                                     "url": url,
                                     "messenger_extensions": True,
                                     "webview_height_ratio": "tall",
                                     "fallback_url": url                                     }
                                     ]
                         },
                         {
                         "title": "IronMan 3",
                         "image_url": "https://images.tenplay.com.au/~/media/TV%20Shows/Movies%20Hub/Movies_Logo_500x281.jpg",
                         "subtitle": "100% Cotton, 200% Comfortable",
                         "default_action": {
                         "type": "web_url",
                         "url": url,
                         "messenger_extensions": True,
                         "webview_height_ratio": "tall",
                         "fallback_url": url
                         },
                         "buttons": [
                                     {
                                     "title": "Watch Now",
                                     "type": "web_url",
                                     "url": url,
                                     "messenger_extensions": True,
                                     "webview_height_ratio": "tall",
                                     "fallback_url": url
                                     }
                                     ]
                         },
                         {
                         "title": "Avengers 2",
                         "image_url": "https://images.tenplay.com.au/~/media/TV%20Shows/Movies%20Hub/Movies_Logo_500x281.jpg",
                         "subtitle": "100% Cotton, 200% Comfortable",
                         "default_action": {
                         "type": "web_url",
                         "url": url,
                         "messenger_extensions": True,
                         "webview_height_ratio": "tall",
                         "fallback_url": url
                         },
                         "buttons": [
                                     {
                                     "title": "Watch Now",
                                     "type": "web_url",
                                     "url": url,
                                     "messenger_extensions": True,
                                     "webview_height_ratio": "tall",
                                     "fallback_url": url
                                     }
                                     ]
                         },
                         {
                         "title": "I am Groot",
                         "image_url": "https://images.tenplay.com.au/~/media/TV%20Shows/Movies%20Hub/Movies_Logo_500x281.jpg",
                         "subtitle": "100% Cotton, 200% Comfortable",
                         "default_action": {
                         "type": "web_url",
                         "url": url,
                         "messenger_extensions": True,
                         "webview_height_ratio": "tall",
                         "fallback_url": url
                         },
                         "buttons": [
                                     {
                                     "title": "Watch Now",
                                     "type": "web_url",
                                     "url": url,
                                     "messenger_extensions": True,
                                     "webview_height_ratio": "tall",
                                     "fallback_url": url
                                     }
                                     ]
                         }
                         ],
              "buttons": [
                          {
                          "title": "View More",
                          "type": "postback",
                          "payload": "payload"
                          }
                          ]
    }
}
}

}
}
  
  value = recevied_message.lower()
  if value in responses:
    print("-----------------------ERROR")
    txt_back = responses[value]
  else:
    txt_back = {"recipient":{"id":fbid}, "message":{"text": "I didin't understand you. Sorry! Type 'Help' to see my features! :)"}}
  
  
  response_msg = json.dumps(txt_back)
  status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
  pprint(status.json())
