#EmailAssistant

Pretty Simple Script that uses the Nylas api to gather recent email then uses NLTK package to clean up and tokenize mail content, finally 
a sequence of for and if statements indicate if the Nylas api will be used to sent a mail. I have a gmail extension that autobccs to a dummy email.
I use a server that runs the script every 10 min.
When the script is run it looks at the most recent mails in the dummy email and send the corresponding email to the receiver of the mail.


##TODO
Add an abstraction layer to allow users to customize amount of emails
Learn more NLP techniques which will do away with for and if statements
Build a front end with customizeable name and assistant name
Find a way to not use bcc extension to a dummy email
Find a way to do away with dummy account
