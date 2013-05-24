=Fullonsms python command line client (python) by vengadanathan=

1.Register with fullonsms.com to get username i.e(your mobile number) and password , then
use this command line tool to send sms
Note:
SMS can be sent only between 8.00AM to 8.00PM for DND disabled mobile numbers.

Usage:
{{{
$ python fullonsms.py
usage: fullonsms.py [-h] -u USERNAME -p PASSWORD [-m MESSAGE] [-t TO]
                   [--about]
fullonsms.py: error: argument -u/--username is required
}}}

=Example:=

python fullonsms.py -u 999999999 -p hhhh -m "Test Message"


EnjoY