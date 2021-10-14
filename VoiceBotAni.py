import pyttsx3
import smtplib
import speech_recognition as sr

from email.message import EmailMessage    #accessing message bodies, and for creating or modifying structured  messages.


listener = sr.Recognizer()  #To recognise whatsoever we are saying
engine = pyttsx3.init()


def talk(text):
    engine.say(text)        #To Make engine speak texts
    engine.runAndWait()     #To make this Execute and then wait


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)
            # listener.dynamic_energy_threshold = False
            voice = listener.listen(source, phrase_time_limit=7, timeout=8)
            print("**DONE**")
            info = listener.recognize_google(voice)    #Google API to convert voice to text
            print(info)
            return info.lower()
    except:
        print('Try Again')


email_list = {
    'sumit': 'sumittripathi508@gmail.com',
    'dev': 'awadhesh.narain200@gmail.com',
    'ma': 'mradulatripathi2000@gmail.com',
    'yash': 'apratim.tr@gmail.com',
    'ankur': 'ankurgopalyadav1312@gmail.com',
}


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)    #Providing server name and THE port number on which it will work
    server.starttls()                               #turn an insecure connection into a secure one
    server.login('shivlitownorganisation@gmail.com', 'user pass')
    email = EmailMessage()
    email['From'] = 'shivlitownorganisation@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


def get_email_info():
    talk('Welcome sir I know you are here to send an email So Now Please tell me')
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('is the reciever name present in the list')
    reclist = get_info()
    if 'no' in reclist:
        name = get_info()
    else:
        receiver = email_list[name]    
    talk('What is the subject of your email?')
    subject = get_info()
    talk('is the subject correct ?')
    subrit = get_info()
    if 'no' in subrit:
        subject = get_info()
    else:
        talk('Ok')
    talk('Tell me the text in your email')
    message = get_info()
    talk('is the printed text is what you want to send ?')
    messrit = get_info()
    if 'no' in messrit:
        message = get_info()
    else:
        talk('ok')
    send_email(receiver, subject, message)
    talk('Hey! Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

get_email_info()
