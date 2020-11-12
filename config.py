import os
class Config(object):
	BOT_TOKEN = os.environ.get('BOT_TOKEN', '1476773425:AAH3XVG13N7P2v__IKmo8JrJbfcNIGef20Q)
	GUSERNAME = os.environ.get('GUSER_NAME', 'deadyt8309@gmail.com')
	GPASSWORD = os.environ.get('GPASSWORD', '+919835495101')

# If you're not familiar with how to set Environment Variables you can do like this instead
# of  setting Environment Variables

# BOT_TOKEN = os.environ.get('BOT_TOKEN', 'BOT_TOKEN_HERE')
# GUSERNAME = os.environ.get('GUSER_NAME', 'Google Email')
# GPASSWORD = os.environ.get('GPASSWORD', 'Google Email Password')

#NOTE: Putting sensitive information in files is considered unsafe. Try to use ENVIRONMENT VARIABLES 
