from bs4 import BeautifulSoup
from urllib2 import Request
import urllib2
import smtplib
import time
from time import sleep

def rates_fetcher(url):
	html = urllib2.urlopen(Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })).read()
	soup = BeautifulSoup(html)
	return [item.text for item in soup.find_all(class_='rightCol')]

def sendMail(msg):
	sender = 'no-reply@currency.com'
	receivers = ['example@example.com']
	message = "From: Currency <%s>\nTo: Da Boss <%s>\nSubject:%s\n\n%s" % (sender,receivers,msg,msg)

	try:
		smtpObj = smtplib.SMTP('localhost')
		smtpObj.sendmail(sender, receivers, message)
		print "Successfully sent email"
	except SMTPException:
		print "Error: unable to send email"


while 1:
	url1 = "http://www.xe.com/currencyconverter/convert/?Amount=1&From=MYR&To=THB"
	now = time.strftime("%c")
	nowdatetime = time.strftime("%c")
	rate = rates_fetcher(url1)
	rate = rate[0].encode('ascii', 'ignore').split('\n')[0]
	message = "RM1 to %s - %s" % (rate,nowdatetime)
	sendMail(message)
	sleep(3600)
