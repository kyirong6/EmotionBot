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
    print("\n\n\n-----------------------------JSON---------------\n\n\n")
    print(incoming_message)
    print("-----------------------------JSON---------------\n\n\n")
    id = incoming_message['entry'][0]['messaging'][0]['sender']['id']
    if 'postback' in incoming_message['entry'][0]['messaging'][0]:
      payload = incoming_message['entry'][0]['messaging'][0]['postback']['payload']
      if payload == "Startup":
        print("yay omg")
        post_facebook_message(str(id), 'startup')
        post_facebook_message(str(id),'load')
        post_facebook_message(str(id), 'startup2')
        post_facebook_message(str(id),'load')
        post_facebook_message(str(id), 'startup3')
        return HttpResponse(200)
      if payload == "Happy":
        post_facebook_message(str(id),'load')
        post_facebook_message(str(id),'happy')
        return HttpResponse(200)
      if payload == "Sad":
        post_facebook_message(str(id),'load')
        post_facebook_message(str(id), 'sad')
        return HttpResponse(200)
      if payload == "Motivating":
        post_facebook_message(str(id),'load')
        post_facebook_message(str(id), 'motivating')
        return HttpResponse(200)
      if payload == "General":
        post_facebook_message(str(id),'load')
        post_facebook_message(str(id), 'general')
        return HttpResponse(200)
      if payload == "Emotions":
        post_facebook_message(str(id),'load')
        post_facebook_message(str(id), 'emotions')
        return HttpResponse(200)
      if payload == "Write":
        print("weird..?")
        post_facebook_message(str(id),'load')
        post_facebook_message(str(id), 'write')
        return HttpResponse(200)
      if payload == "Guide":
        post_facebook_message(str(id),'load')
        post_facebook_message(str(id), 'guide')
        return HttpResponse(200)
      if payload == "Options":
        post_facebook_message(str(id),'load')
        post_facebook_message(str(id), 'startup3')
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
              print("------------------- I AM A SPLITTER {a}".format(a=1))
              print(type(str(message['sender']['id'])))
              post_facebook_message(str(message['sender']['id']), message['message']['text'])
    return HttpResponse(200)

def post_facebook_message(fbid, recevied_message):
  #  client = textrazor.TextRazor(extractors=["entities", "topics"])
  #  response = client.analyze("I am really sad right now".decode('utf-8'))
  #  #print(response.entities())
  #
  #  for entity in response.entities():
  #      print(entity)
  post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAR79XI6ZBqUBAAUhLg2LChl0xI8j4lZC4fIOZAFic9O4Kl0xJYUnCJW81G5kcdZAVBPOepprGCn8Bm4WkRdHs3Pn52IqtDnIlsLq2LIDGro91sFo0Dlz7SsYWkFlvaSu0qnFSxgbnUI22QX8lIgJdZBvkRaM1EPtqgDegqPOIgZDZD'
  url = "https://petersapparel.parseapp.com"
  
  #user_details_url = "https://graph.facebook.com/v2.8/" + fbid
  #user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':'<page-access-token>'}
  # user_details = requests.get(user_details_url, user_details_params).json()
  # print(user_details)
  # name = user_details['first_name']
  
  
  
  responses = {'general':{"recipient":{"id":fbid}, "message":{"text": "General"}},
    'emotions': {"recipient":{"id":fbid}, "message":{"text": "Emotions"}},
      'guide': {"recipient":{"id":fbid}, "message":{"text": "guide"}},
        'write': {"recipient":{"id":fbid}, "message":{"text": "write"}},
        'load': {
      "recipient":{
        "id":fbid
  },
    "sender_action":"typing_on"
    },
      'startup': {"recipient":{"id":fbid}, "message":{"text": "Hey Choenden! Welcome to my platform. I can help you in a variety of ways depending on your mood and can even log some journals for you. :)"}} ,
        'startup2':{"recipient":{"id":fbid}, "message":{"text": "Tell me things like: \n\n I want happy stuff \n I want sad stuff \n I want motivating stuff \n\n Or choose from the options below or enter 'Help'."}}  ,
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
                    "title":"Moods and Emotions",
                    "subtitle":"A space just for you",
                    "image_url":"http://vignette1.wikia.nocookie.net/theomegascapers/images/3/36/Sun_and_Moon_by_daydreamer_art.jpg/revision/latest?cb=20120720172022",
                    "buttons":[
                               {
                               "type":"postback",
                               "payload":"Happy",
                               "title":"Happy"
                               },
                               {
                               "type":"postback",
                               "title":"Sad",
                               "payload":"Sad"
                               },
                               {
                               "type":"postback",
                               "title":"Motivating",
                               "payload":"Motivating"
                               }
                               ]
                    },
                    {
                    "title":"My Journal",
                    "subtitle":"Express yourself",
                    "image_url" : "http://img14.deviantart.net/9dca/i/2012/231/f/9/deep_thoughts_by_artilin-d5bnm6i.jpg",
                    "buttons":[
                               {
                               "type":"postback",
                               "payload":"Write",
                               "title":"Write"
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
        "template_type":"generic",
        "elements":[
                    {
                    "title":"What Do I Do?",
                    "subtitle":"Information for you",
                    "buttons":[
                               {
                               "type":"postback",
                               "payload":"General",
                               "title":"General"
                               },
                               {
                               "type":"postback",
                               "title":"The Emotions",
                               "payload":"Emotions"
                               },
                               {
                               "type":"postback",
                               "title":"Options",
                               "payload":"Options"
                               }
                               
                               ]
                    },
                    {
                    "title":"What's 'My Journal'?",
                    "subtitle":"A guide",
                    "buttons":[
                               {
                               "type":"postback",
                               "payload":"Guide",
                               "title":"Our Goal Together"
                               }
                               ]
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
    txt_back = responses[value]
  else:
    txt_back = {"recipient":{"id":fbid}, "message":{"text": "I didin't understand you. Sorry! Type 'Help' to see my features! :)"}}
  
  
  response_msg = json.dumps(txt_back)
  status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
  print("\n\n\n-----------------------------STATUS---------------\n\n\n")
  pprint(status.json())
  print("-----------------------------STATUS---------------\n\n\n")
