import json, requests, random, re
import textrazor
from pprint import pprint

from django.views import generic
from django.http.response import HttpResponse



class Facebook:
  
  @staticmethod
  def post_facebook_message(fbid, recevied_message):
    #  client = textrazor.TextRazor(extractors=["entities", "topics"])
    #  response = client.analyze("I am really sad right now".decode('utf-8'))
    #  #print(response.entities())
    #
    #  for entity in response.entities():
    #      print(entity)
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAR79XI6ZBqUBAAUhLg2LChl0xI8j4lZC4fIOZAFic9O4Kl0xJYUnCJW81G5kcdZAVBPOepprGCn8Bm4WkRdHs3Pn52IqtDnIlsLq2LIDGro91sFo0Dlz7SsYWkFlvaSu0qnFSxgbnUI22QX8lIgJdZBvkRaM1EPtqgDegqPOIgZDZD'
    url="https://petersapparel.parseapp.com"
    youtubeurl1="https://www.youtube.com/watch?v=y6Sxv-sUYtM"
    youtubeurl2="https://www.youtube.com/watch?v=4N3N1MlvVc4"
    viewurl1="https://au.pinterest.com/search/pins/?q=happy&rs=typed&term_meta[]=happy%7Ctyped"
    viewurl2="https://au.pinterest.com/search/pins/?q=sad&rs=typed&term_meta[]=sad%7Ctyped"
    movieurl1="https://www.justwatch.com/au/provider/stan?genres=cmy,fml"
    movieurl2="https://www.justwatch.com/au/provider/stan?genres=war,hrr,rma,drm"
    shopurl1="https://www.amazon.com/"
    
    
    
    
    
    #user_details_url = "https://graph.facebook.com/v2.8/" + fbid
    #user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':'<page-access-token>'}
    # user_details = requests.get(user_details_url, user_details_params).json()
    # print(user_details)
    # name = user_details['first_name']
    cute = {
  "recipient":{
    "id":fbid
  }, "message": {
    "attachment": {
      "type": "template",
        "payload": {
          "template_type": "list",
            "top_element_style": "compact",
            "elements": [
                         {
                         "title": "Ingrid Michaelson - They Way I Am",
                         "image_url": "http://www.mtv.com/crop-images/2013/09/04/ingrid-michaelson-shervin-lainez-2010-rgb.jpg",
                         "subtitle": "Enjoy this happy song we found for you",
                         "default_action": {
                         "type": "web_url",
                         "url": youtubeurl1,
                         "messenger_extensions": True,
                         "webview_height_ratio": "tall",
                         "fallback_url": youtubeurl1
                         },
                         "buttons": [
                                     {
                                     "title": "Listen",
                                     "type": "web_url",
                                     "url": youtubeurl1,
                                     "messenger_extensions": True,
                                     "webview_height_ratio": "tall",
                                     "fallback_url": youtubeurl1                                     }
                                     ]
                         },
                         {
                         "title": "Explore Some Pins",
                         "image_url": "https://s-media-cache-ak0.pinimg.com/564x/75/47/a1/7547a12cf5e71cfea982ccf15deece9d.jpg",
                         "subtitle": "The options are endless",
                         "default_action": {
                         "type": "web_url",
                         "url": viewurl1,
                         "messenger_extensions": True,
                         "webview_height_ratio": "tall",
                         "fallback_url": viewurl1
                         },
                         "buttons": [
                                     {
                                     "title": "View",
                                     "type": "web_url",
                                     "url": viewurl1,
                                     "messenger_extensions": True,
                                     "webview_height_ratio": "tall",
                                     "fallback_url": viewurl1
                                     }
                                     ]
                         },
                         {
                         "title": "Watch some movies",
                         "image_url": "http://www.herinterest.com/wp-content/uploads/2015/01/20-Cute-Romance-Movies_10.jpg",
                         "subtitle": "Here's what we recommend",
                         "default_action": {
                         "type": "web_url",
                         "url": movieurl1,
                         "messenger_extensions": True,
                         "webview_height_ratio": "tall",
                         "fallback_url": movieurl1
                         },
                         "buttons": [
                                     {
                                     "title": "Dive In",
                                     "type": "web_url",
                                     "url": movieurl1,
                                     "messenger_extensions": True,
                                     "webview_height_ratio": "tall",
                                     "fallback_url": movieurl1
                                     }
                                     ]
                         },
                         {
                         "title": "Treat Yourself",
                         "image_url": "https://www.hackerx.org/jobs/wp-content/uploads/2013/06/Amazon-logo.png",
                         "subtitle": "Shopping Is Easy",
                         "default_action": {
                         "type": "web_url",
                         "url": shopurl1,
                         "messenger_extensions": True,
                         "webview_height_ratio": "tall",
                         "fallback_url": shopurl1
                         },
                         "buttons": [
                                     {
                                     "title": "View",
                                     "type": "web_url",
                                     "url": shopurl1,
                                     "messenger_extensions": True,
                                     "webview_height_ratio": "tall",
                                     "fallback_url": shopurl1
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
  happy = {
  "recipient":{
    "id":fbid
}, "message": {
  "attachment": {
    "type": "template",
      "payload": {
        "template_type": "list",
          "top_element_style": "compact",
            "elements": [
                         {
                         "title": "Happy - Pharrell Williams",
                         "image_url": "https://upload.wikimedia.org/wikipedia/en/2/23/Pharrell_Williams_-_Happy.jpg",
                         "subtitle": "Enjoy this happy song we found for you",
                         "default_action": {
                         "type": "web_url",
                         "url": youtubeurl1,
                         "messenger_extensions": True,
                         "webview_height_ratio": "tall",
                         "fallback_url": youtubeurl1
                         },
                         "buttons": [
                                     {
                                     "title": "Listen",
                                     "type": "web_url",
                                     "url": youtubeurl1,
                                     "messenger_extensions": True,
                                     "webview_height_ratio": "tall",
                                     "fallback_url": youtubeurl1                                     }
                                     ]
                         },
                         {
                         "title": "Explore Some Pins",
                         "image_url": "https://s-media-cache-ak0.pinimg.com/736x/96/26/33/962633096e9f47451bdc6131656a3fa4.jpg",
                         "subtitle": "The options are endless",
                         "default_action": {
                         "type": "web_url",
                         "url": viewurl1,
                         "messenger_extensions": True,
                         "webview_height_ratio": "tall",
                         "fallback_url": viewurl1
                         },
                         "buttons": [
                                     {
                                     "title": "View",
                                     "type": "web_url",
                                     "url": viewurl1,
                                     "messenger_extensions": True,
                                     "webview_height_ratio": "tall",
                                     "fallback_url": viewurl1
                                     }
                                     ]
                         },
                         {
                         "title": "Watch some movies",
                         "image_url": "http://www.classic-play.com/wp-content/uploads/2012/06/happy-poster-preview.jpg",
                         "subtitle": "Here's what we recommend",
                         "default_action": {
                         "type": "web_url",
                         "url": movieurl1,
                         "messenger_extensions": True,
                         "webview_height_ratio": "tall",
                         "fallback_url": movieurl1
                         },
                         "buttons": [
                                     {
                                     "title": "Dive In",
                                     "type": "web_url",
                                     "url": movieurl1,
                                     "messenger_extensions": True,
                                     "webview_height_ratio": "tall",
                                     "fallback_url": movieurl1
                                     }
                                     ]
                         },
                         {
                         "title": "Treat Yourself",
                         "image_url": "https://www.hackerx.org/jobs/wp-content/uploads/2013/06/Amazon-logo.png",
                         "subtitle": "Shopping Is Easy",
                         "default_action": {
                         "type": "web_url",
                         "url": shopurl1,
                         "messenger_extensions": True,
                         "webview_height_ratio": "tall",
                         "fallback_url": shopurl1
                         },
                         "buttons": [
                                     {
                                     "title": "View",
                                     "type": "web_url",
                                     "url": shopurl1,
                                     "messenger_extensions": True,
                                     "webview_height_ratio": "tall",
                                     "fallback_url": shopurl1
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
  sad = {
  "recipient":{
    "id":fbid
}, "message": {
  "attachment": {
    "type": "template",
      "payload": {
        "template_type": "list",
          "top_element_style": "compact",
            "elements": [
                         {
                         "title": "Mad World - Gary Jules",
                         "image_url": "http://images.amazon.com/images/P/B0001IXTOU.01.LZZZZZZZ.jpg",
                         "subtitle": "Enjoy this happy song we found for you",
                         "default_action": {
                         "type": "web_url",
                         "url": youtubeurl2,
                         "messenger_extensions": True,
                         "webview_height_ratio": "tall",
                         "fallback_url": youtubeurl2
                         },
                         "buttons": [
                                     {
                                     "title": "Listen",
                                     "type": "web_url",
                                     "url": youtubeurl2,
                                     "messenger_extensions": True,
                                     "webview_height_ratio": "tall",
                                     "fallback_url": youtubeurl2                                     }
                                     ]
                         },
                         {
                         "title": "Explore Some Pins",
                         "image_url": "http://www.publicdomainpictures.net/pictures/20000/nahled/sad-man-and-rain.jpg",
                         "subtitle": "The options are endless",
                         "default_action": {
                         "type": "web_url",
                         "url": viewurl2,
                         "messenger_extensions": True,
                         "webview_height_ratio": "tall",
                         "fallback_url": viewurl2
                         },
                         "buttons": [
                                     {
                                     "title": "View",
                                     "type": "web_url",
                                     "url": viewurl2,
                                     "messenger_extensions": True,
                                     "webview_height_ratio": "tall",
                                     "fallback_url": viewurl2
                                     }
                                     ]
                         },
                         {
                         "title": "Watch some movies",
                         "image_url": "https://s-media-cache-ak0.pinimg.com/originals/8b/5d/0b/8b5d0b948c67f2dee3a42b0b985b4f76.jpg",
                         "subtitle": "Here's what we recommend",
                         "default_action": {
                         "type": "web_url",
                         "url": movieurl2,
                         "messenger_extensions": True,
                         "webview_height_ratio": "tall",
                         "fallback_url": movieurl2
                         },
                         "buttons": [
                                     {
                                     "title": "Dive In",
                                     "type": "web_url",
                                     "url": movieurl2,
                                     "messenger_extensions": True,
                                     "webview_height_ratio": "tall",
                                     "fallback_url": movieurl2
                                     }
                                     ]
                         },
                         {
                         "title": "Binge Eat",
                         "image_url": "https://pbs.twimg.com/profile_images/727390716192657408/2z3TnDsT.jpg",
                         "subtitle": "Only A Click Away",
                         "default_action": {
                         "type": "web_url",
                         "url": shopurl1,
                         "messenger_extensions": True,
                         "webview_height_ratio": "tall",
                         "fallback_url": shopurl1
                         },
                         "buttons": [
                                     {
                                     "title": "View",
                                     "type": "web_url",
                                     "url": shopurl1,
                                     "messenger_extensions": True,
                                     "webview_height_ratio": "tall",
                                     "fallback_url": shopurl1
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
  startup3 = {
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
                                 "title":"Cute",
                                 "payload":"Cute"
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
  }
    help = {
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
  }
    
    
    
    responses = {'cute': cute,
      'message': {"recipient":{"id":fbid}, "message":{"text": "Here are some things we found for you..."}},
      'message2': {"recipient":{"id":fbid}, "message":{"text": "According to our calculations you've had a positive entry! Here are some things for you..."}},
        'message3': {"recipient":{"id":fbid}, "message":{"text": "According to our calculations you've had an entry more on the negative side. Here are some things for you..."}},
      'positive': happy,
      'negative': sad,
      'neutral': {"recipient":{"id":fbid}, "message":{"text": "You are Neutral :) The options are up to you!"}},
      'general':{"recipient":{"id":fbid}, "message":{"text": "Hey There... I'm your personal bot and I'm here to support your moods and brighten up your day if you need me.\n\nI feed you music, movies, food, shopping opportunities, and even journal entries. \n\nClick on 'The Emotions' or 'Our Goal Together' to learn more!"}},
      
      'emotions': {"recipient":{"id":fbid}, "message":{"text": "For now we can cater to: \n\nHappy\nSad\nCute\n\nWith the touch of a button we will give you recommendations that will support your moods such as movies, food and shopping opportunities.\n\nRather than having to do many different searches for your state of mind, our chatbot can give you exactly what you need when you need it."}},
        'guide': {"recipient":{"id":fbid}, "message":{"text": "Use your journal to tell me how your day went and I'll give you a report and keep track of how your mood has changed throughout our little chats. \nWe are using tools such as:\n\n Sentiment Analysis\n Natural Language Processing\n Tone Analysis\n\nThis space is a safe place for you and whatever you need. :)"}},
          'write': {"recipient":{"id":fbid}, "message":{"text": "Hi there. Welcome to Your Journal. Here is a space where you can write an entry whenever you please and recieve back an analysis of your text.\nSpecifically, we will be performing: \n\nNLP\nSentiment Analysis\nTone Analysis\n\nPlease write here and enter here."}},
          'load': {
        "recipient":{
          "id":fbid
  },
    "sender_action":"typing_on"
      },
        'startup': {"recipient":{"id":fbid}, "message":{"text": "Hey Choenden! Welcome to my platform. I can help you in a variety of ways depending on your mood and can even log some journals for you. :)"}} ,
          'startup2':{"recipient":{"id":fbid}, "message":{"text": "Tell me things like: \n\n I want happy stuff \n I want sad stuff \n I want motivating stuff \n\nOr choose from the options below or enter 'Help'."}},
            
            'i want cute stuff' : cute,
            'i want happy stuff' : happy,
            'i want sad stuff' : sad,
            'startup3': startup3,
            'happy': happy,
            'sad': sad,
            'help': help

}
  value = recevied_message.lower()
    if (value in responses):
      txt_back = responses[value]
  else:
    txt_back = {"recipient":{"id":fbid}, "message":{"text": "I didin't understand you. Sorry! Type 'Help' to see my features! :)"}}
    
    
    response_msg = json.dumps(txt_back)
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    print("\n\n\n-----------------------------STATUS---------------\n\n\n")
    pprint(status.json())
    print("\n\n\n-----------------------------STATUS---------------\n\n\n")


