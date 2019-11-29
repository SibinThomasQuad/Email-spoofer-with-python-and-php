import requests
TGREEN =  '\033[32m' # Green Text
print(TGREEN+"###########################################################\n")
print("###################-EMAIL SPOOFER-#########################\n")
print("###########################################################\n")
toemail = raw_input("Please enter the destination email address\n>")
subject = raw_input("Please enter subject\n>")
message= raw_input("Please enter the message\n>")
fromemail = raw_input("Please enter the spoofed email address\n>")
fromname = raw_input("Please enter the spoofed name\n>")
url="https://example.com/mail/mailer.php?toemail="+toemail+"&subject="+subject+"&message="+message+"&fromemail="+fromemail+"&fromname="+fromname
data = requests.get(url).json
