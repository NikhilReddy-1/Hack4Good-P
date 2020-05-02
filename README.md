# Hack4Good-P
Live COVID-19 Stats mailing system.

## Required packages

	smtplib
	os
	numpy
	matplotlib
	flask
	request

## Usuage 

	python final.py
	
	The user ID and Password for the mail were stored in local variables on the machine and were imported through OS library
	
	
## Input 

	Enter your E-mail ID:
	Enter your state:
	Enter your district:
	
	
## Functions 

	def getresponse()
		opens url
		checks if it is able to access data(i.e. 200 'ok')
		if yes, loads data into jsonData
		else responds with error message
		
	def main()
		loads json database from the covid19 GOI links using getResponse
		#Counting no. of cases in user's area
		1st loop - 
		iterating through key values from collected database and storing it in x
		1st if condition - 
		compare the user input for state with current key value x.
		if statisfied, load the dictionary of the state in y. else increment i
		2nd loop - 
		iterating through key values from state database and store district value in k.
		2nd if condition -
		compare the user input for district with current key value k.
		if statisfied, load the required data from dictionary, else increment t.
		data loaded - active cases, confirmed cases, recovered cases and deceased cases.
		
		#Counting no. cases of cases all over India
		1st loop - 
		iterates through every district in every state
		2nd loop - 
		iterates through every data stored in distrcit dictionary
		adds total to previous district's total
		
		In the smtplib. We call the SMTP_SSL protocol with the gmail server and port number 465.
		
		We use the smtp.login function to log into the sender e-mail ID. This function has to be passed 2 arguments which are the EMAIL_ID and EMAIL_PASS.
		
		The value for both these variables should not be visible in the code for security purposes of the account holder, so the 
		values of these variables are called from the OS, these values are stored as environment variables in the .bash_profile file on the system
		smtp.sendmail() function has to be passed 3 arguments, which are:
		SENDER i.e. Sender E-mail ID,in our case it is the variable EMAIL_ID. We get the value of that code from an OS environment variable for security purposes of the account.
		RECEIVER i.e. The user e-mail ID, we use a variable called as RECEIVER which get's it's value from user input.
		msg i.e. the content of the e-mail, we get the value of this from combining two different strings which are {subject {body}.
		
		In the message body we have 2 different strings for Red Zone qualification criteria i.e. more than 15 active cases in a district.
		
		

## Description Link:

	https://drive.google.com/drive/folders/1zWDbCDb1Sn8GOEgCW4nipzM9A0D50M4W?usp=sharing


We use the SMTP library to send the Email to the User

We have used crowdsourced database for the system:

	https://api.covid19india.org/v2/state_district_wise.json
	https://api.covid19india.org/data.json
