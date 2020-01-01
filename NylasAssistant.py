import re, string, unicodedata
import nltk
nltk.download('punkt')
import contractions
#import inflect

from bs4 import BeautifulSoup

from nltk import word_tokenize, sent_tokenize
from nylas import APIClient


#Variable Definitions

assistantname = "Debbie"
#location = []

#Function Definitions

#Noise Removal 
def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

def replace_contractions(text):
    """Replace contractions in string of text"""
    return contractions.fix(text)

def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    text = replace_contractions(text)
    return text

# Main
nylas = APIClient(
    "6ihfb5rh4uw0iwgops0qj2v57",
    "9d2373w0eu8w4r1y7vjbljurm",
    "4tfloptd6mbcf5sc8bpbz6ye7"
)



# Return most recent emails on the linked account

for message in nylas.messages.where(limit=1):
    #print(message)

    text = denoise_text(message.body)
    text = nltk.word_tokenize(text)
    print(text)
    
    for i in range(0,len(text)):
        location = []
        if text[i] == assistantname and text[i+1] == "," and text[i+2] == "tell" and text[i+3] == "this":
            for j in range(i + 5, i + 15):
                if text[j] == "to" and (text[j + 1] == "reach") or (text[j + 1] == "link" and text[j + 2] == "up") or (text[j + 1] == "come" and text[j + 2] == "through"):
                    #Send email to person noting the creation of a contact
                    draft = nylas.drafts.create()
                    draft.subject = "Meeting"
                    draft.body = "Hello, I'm " + assistantname + ", Victor's assistant. <br> <br> Victor would like to set up a meeting with you. <br> <br> Here are his availabilities for the next 2 weeks. <br> <br> schedule.nylas.com/victor-awogbemi-30min <br> <br> Sincerely, "+ assistantname  
                    draft.to = message.to

                    draft.send()
                if text[j] == "reach" or (text[j] == "link" and text[j + 1] == "up") or (text[j] == "come" and text[j + 1] == "through")  and (text[j+1] == "to" or text[j+2] == "to"):
                    for k in range(j + 2, j + 11):
                        if text[k] == ",":
                            break
                        elif text[k] != "to":
                            location.append(text[k])

                            
                                
                    




        #Create Contact
        if text[i] == assistantname and text[i+1] == "," and text[i+2] == "add" and text[i+3] == "this":

            #Creates Contact
            '''contact = nylas.contacts.create()
            contact.given_name = "My"
            contact.middle_name = "Nylas"
            contact.surname = "Friend"
            contact.emails['work'] = ['swag@nylas.com']

            contact.save()'''

            #Send Mail
            draft = nylas.drafts.create()
            draft.subject = "Contacts"
            draft.body = "Hello, I'm " + assistantname + ", Victor's assistant. <br> <br> This email is to notify you that Victor has added you to his contacts. <br> <br> Sincerely, "+ assistantname  
            draft.to = message.to

            draft.send()

        if text[i] == assistantname and text[i+1] == "," and (text[i+2] == "nize" or text[i+2] == "cut")  and text[i+3] == "this":
       
            #Send Mail
            draft = nylas.drafts.create()
            draft.subject = "Your Account has been blocked"
            draft.body = "Hello, I'm " + assistantname + ", Victor's assistant. <br> <br> This email is to notify you that Victor has blocked you. <br> <br> Sincerely, "+ assistantname 
            draft.to = message.to

            draft.send()

        if "pham" in message.snippet:
            draft = nylas.drafts.create()
            draft.subject = "With Love, from Nylas"
            draft.body = "This email was sent using the Nylas Email API. Visit https://nylas.com for details."
            draft.to = [{'name': 'My Nylas Friend', 'email': 'vawogbemi@gmail.com'}]

            draft.send()

        if "pham" in message.snippet:
            draft = nylas.drafts.create()
            draft.subject = "With Love, from Nylas"
            draft.body = "This email was sent using the Nylas Email API. Visit https://nylas.com for details."
            draft.to = [{'name': 'My Nylas Friend', 'email': 'vawogbemi@gmail.com'}]

            draft.send()
