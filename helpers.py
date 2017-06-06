from enum import Enum
from security import Password
class LOG_keywords(Enum):
	LOG_FILE_LOCATION = "/home/divyanshu/Voylla/website/production.log" # "/mnt/voylla-staging/current/log/staging.log"
	LOG_DIRECTORY = "/home/divyanshu/Voylla/website/staging.log." #"/mnt/voylla-staging/current/log/staging.log." 
	MAIL_SUBJECT = ["422 ERROR LOG DETAILS","500 ERROR LOG DETAILS"]
	MAIL_FROM = ['divyanshu.voylla@gmail.com','divyanshu.voylla@gmail.com']
	MAIL_TO = ["divyanshu.voylla@gmail.com","divyanshu.voylla@gmail.com"]
	MAIL_PASSWORD  = [Password.p.value,Password.p.value]

class LOG_Patterns(Enum):
	NO_OF_ERRORS = 2
	REQUEST_LINE = [("Started GET" and "Started PATCH"),("Started GET" or "Started PATCH" or "Started POST")]
	ACTION = ["ActionController","ActiveRecord"]
	ERROR_PHRASE = ["Completed 422 Unprocessable Entity","Completed 500 Internal Server"]

class Cron_keywords(Enum):
	ods_file_path = "/home/divyanshu/Voylla/website/cron.ods"
	log_file_path = "/home/divyanshu/Voylla/website/syslog"
	MAIL_SUBJECT = ["CRON IS NOT WORKING !!!"]
	MAIL_FROM = ['']
	MAIL_TO = [""]
	MAIL_PASSWORD  = [""]
	sheet_name = "Sheet3"