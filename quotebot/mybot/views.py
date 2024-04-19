

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from .quote import fetch_random_quote
from dotenv import load_dotenv
import os

@csrf_exempt
# def twilio_webhook(request):
def home(request):
    load_dotenv()
    account_sid = os.environ.get("ACCOUNT_SID")
    print(f"ACCOUNT SID = {account_sid}")
    auth_token = os.environ.get("AUTH_TOKEN")
    twilio_number = os.environ.get("TWILIO_NUMBER")


    client = Client(account_sid, auth_token)
    if request.method == "POST":
        message = request.POST
        user_name = message["ProfileName"]
        User_number = message["From"]
        user_msg = message["Body"]

        if user_msg.lower() in ["hi", "hello", "hey", "h"]:
            client.messages.create(
                from_ = f"whatsapp:{twilio_number}",   #initiator
                body = f"Hey {user_name}",
                to = User_number        #receievr              
            )

        elif "quote" in user_msg.lower():
            category = user_msg[5:].strip()
            user_quote = fetch_random_quote(category)
            if isinstance(user_quote, str):
                #in the case that fetch random quote returns a str manage.
                client.messages.create(
                        from_ = f"whatsapp:{twilio_number}",   #initiator
                        body = user_quote,
                        to = User_number 
                )

            else:
                choosen_quote = user_quote[0].get("quote")
                choosen_author = user_quote[0].get("author")

                client.messages.create(
                        from_ = f"whatsapp:{twilio_number}",   #initiator
                        body = f"QUOTE: {choosen_quote}\nAUTHOR: {choosen_author}",
                        to = User_number 
                )

        
        else:
            client.messages.create(
                            from_ = f"whatsapp:{twilio_number}",   #initiator
                            body = f"Invalid input kindly use a valid command ",
                            to = User_number 
                    )



    return render(request, "home.html")






