#fullonsms sms sender
#Keywords python free sms api
#Author Vengadanathan Srinivasan<fantastic.next@gmail.com>
import cookielib, urllib2 , urllib
import httplib
import sys
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-u", "--username", type=str,
                    help="your 10 digit fullonsms registered mobile number",action='store',required=True)
parser.add_argument("-p", "--password", type=str,
                    help="your fullonsms password",action='store',required=True)
parser.add_argument("-m", "--message", type=str,
                    help="message to sent(140 characters maximum)",action='store',) 
parser.add_argument("-t", "--to", type=str,
                    help="Mobile Number to send the message",action='store',)      
parser.add_argument("--about", 
                    help="About this Application",version="""
                    Fullonsms command line sender
                    By
                    Vengadanathan Srinivasan
                    <fantastic.next@gmail.com>

                    """,action='version')    

    
args = parser.parse_args()
#Printing the about 

    
#When the recipient phone number is not given get it from the user    
if args.to is None:
    args.to = raw_input("Enter Mobile number to send the message\n")
    
#When Message is not given get it from the user
if args.message is None:
    print "Enter the Message to send (Enter last line empty to mark end of message) "
    m=""
    sentinel = '' # ends when this string is seen
    for line in iter(raw_input, sentinel):
        m = m +"\n" +line
        pass
    
    args.message =m
           
cj = cookielib.CookieJar()
#Use this to enable debugging
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj),urllib2.HTTPHandler(debuglevel=1))
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#format of post data for login
values = {'MobileNoLogin' : args.username,
      'LoginPassword' : args.password,
      'x':'72',
        'y':'7',
        'redirect':''}
#format the post data to send the sms     
sms ={
'ActionScript':'/home.php',
'CancelScript':'/home.php',
'HtmlTemplate':'/disk1/html/fullonsms/StaticSpamWarning.html',
'MessageLength':'140',
'MobileNos':args.to,
'Message':args.message,
'selTpl':'defaultId',
'Gender':'0',
'FriendName':'Your Friend Name',
'ETemplatesId':'',
'TabValue':'contacts'

}
print "Sending ..."
data = urllib.urlencode(values)
r = opener.open("http://fullonsms.com/")
#Get initial cookies to load
r = opener.open("http://fullonsms.com/login.php")
print "Site Entered"
##print r.info()
opener.addheaders = [('Referer', 'http://fullonsms.com/login.php')]
r = opener.open("http://fullonsms.com/login.php",data)
print "Logged IN"
r = opener.open("http://fullonsms.com/landing_page.php",data)
opener.addheaders = [('Referer', 'http://fullonsms.com/home.php?show=contacts')]
sms = urllib.urlencode(sms)
#posting the message to be sent
r = opener.open("http://fullonsms.com/home.php",sms)
print "SMS Sent"
if 'login' in r.read():
    print "Login Unsuccessful"
else:
    print "Message Sent"



