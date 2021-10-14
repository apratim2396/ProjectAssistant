import speech_recognition as sr
import smtplib
import pyttsx3
import gc
import imaplib
import email
import os
from email.message import EmailMessage
import datetime
import mailbox


listener = sr.Recognizer()
engine = pyttsx3.init()
host ='imap.gmail.com'

                                                                        #user details
your_password = "water is blue"
your_name = "Anivesh"
sender_Email="a##############@gmail.com"
sender_Email_pass="#################"

email_list = {                                                          #list of emails which user have
    'mayank' : 'maya$$$$$$$%@gmail.com',
    'anivesh' : 'an%%%%%%%$$$$$$$@gmail.com'
}

def talk(text):                                                         #function which give output as speech
    engine.say(text)
    engine.runAndWait()

                                    ####################################################
def get_info():                                                         #function to take voice inputs 
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)                   # listener.dynamic_energy_threshold = False
            voice = listener.listen(source, phrase_time_limit=7, timeout=8)
            print("ok.......")
            info = listener.recognize_google(voice)                     #Google API to convert voice to text
            print(info)
            return info.lower()
    except:
        print('Try Again....')
        talk("Try again")

                                    ######################################################

def auth(password):                                                     #function to check the authentication of user
    if password == your_password :
        return 0
    elif password == exit :
        return 2
    else :
        print("Your Password is in correct, Try again .. and if you don't know say EXIt ..")    
        talk("Your Password is in correct, Try again .. and if you don't know say EXIt ..")   
        x = get_info()
        auth(x)

                                    ############################################################

def exit() :                                                            #exit function
    print("bye")        
    talk("bye")

                                    ###########################################################

def send_email(receiver,subject,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()                                                   #make sure to give app acess in google account
    server.login(sender_Email, sender_Email_pass)
    email = EmailMessage()
    email['From'] = sender_Email
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
                                    ####################################################

def get_email_info():                                                   #function to gather the information of email to be send
    print("To Whom you want to send email")
    talk('To Whom you want to send email')
    name = get_info() 
    receiver = email_list[name]
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey , Your email is sent')
    
                                    ########################################################

def get_inbox():                                                        #function to read new emails and mark them read
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(sender_Email, sender_Email_pass)
    mail.list()
    mail.select('inbox')
    result, data = mail.uid('search', None, "UNSEEN") # (ALL/UNSEEN)
    i = len(data[0].split())

    for x in range(i):
        latest_email_uid = data[0].split()[x]
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
                                                                        # result, email_data = conn.store(num,'-FLAGS','\\Seen') 
                                                                        # this might work to set flag to seen, if it doesn't already
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)

                                                                        # Header Details
        date_tuple = email.utils.parsedate_tz(email_message['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
            local_message_date = "%s" %(str(local_date.strftime("%a, %d %b %Y %H:%M:%S")))
        email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
        email_to = str(email.header.make_header(email.header.decode_header(email_message['To'])))
        subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))

                                                                        # Body details
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                print("From: %s\nTo: %s\nDate: %s\nSubject: %s\n\nBody: \n\n%s" %(email_from, email_to,local_message_date, subject, body.decode('utf-8')))
            else:
                continue


                                    ######################################################

os.system("cls")
print("*-"*10)    
print("Welcome to your personal assistance")
talk("Welcome to your personal assistance")
print("*-"*10)    

print("Please Identiye Yourself, say the secret code")
talk("Please Identiye Yourself, say the secret code")
password = get_info()
x= auth(password)
if x == 2 :
    exit()
    
else :
    talk("welcome, ")
    while True :
        gc.collect()
        talk("what can i do for you?")
        print("what can i do for you?")
        p=get_info()
        if (("send" in p) or ("write" in p)) and (("email" in p) or ("gmail" in p) or ("mail" in p)) :
            get_email_info()

        elif (("read" in p) or ("open" in p)) and (("email" in p) or ("gmail" in p)) :
            get_inbox()

        elif (("append" in p) or ("update" in p) or ("add" in p )) and (("list" in p) or ("diary" in p)) :
            print("give the nick name of that person :")
            talk("give the nick name of that person")
            new_name=get_info()
            
            while True :
                print("give the email address of that person :")
                talk("give the email address of that person")
                new_email=get_info()
                talk("listen carefully please and confirm the email address  "+new_email)
                print("listen carefully please and confirm the email Address  " + new_email)
                talk("say yes if confirmed otherwise say no")
                print("say 'YES' if confirmed otherwise say 'NO'")
                confirm =get_info()
                if "yes" in confirm :
                    email_list.update({new_name : new_email})
                    break
                else :
                    continue
        




        elif (("quit" in p) or("exit" in p) )   :
            break

exit()        

