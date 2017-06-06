import smtplib,datetime,pdb
from email.mime.text import MIMEText as text
from helpers import LOG_keywords,LOG_Patterns

i = datetime.datetime.now().isoformat()

file_path = LOG_keywords.LOG_DIRECTORY.value + (i.split("T"))[0] + "/" + ((i.split("T"))[1])[:2] + ".log"  #file_location_of_log_file

with open(file_path) as f:  
		f = f.readlines()  


def send_mail(full_details):  #fucntion for sending mail
		if (isinstance(full_details,list)):
				TEXT = "\n\n"
				for i in range(len(full_details)):
						TEXT = TEXT + """
						REQUESTED-URL: %s
						USER-IP: %s
						ACTIVE-RECORD-TIME: %s
						TIME-STAMP: %s
						ACTION-CONTROL: %s

						
						""" % ((full_details[i])['requested_url'],(full_details[i])['ip'],(full_details[i])['active_record_time'],(full_details[i])['time_stamp'],(full_details[i])['action_control'])
		else:
				TEXT = """
						ERROR: %s
						""" % (full_details)
		# Prepare actual message
		m = text(TEXT)

		m['Subject'] = (LOG_keywords.MAIL_SUBJECT.value)[loop_count]
		m['From'] = (LOG_keywords.MAIL_FROM.value)[loop_count]
		m['To'] = (LOG_keywords.MAIL_TO.value)[loop_count]
		server = smtplib.SMTP(host='smtp.gmail.com', port=587)
		server.starttls()
		server.login((LOG_keywords.MAIL_FROM.value)[loop_count], (LOG_keywords.MAIL_PASSWORD.value)[loop_count])
		server.sendmail(m['From'], m['To'], m.as_string())
		server.quit()

def format_json(json):   #function for formatting data 
	log_details = {}
	for key in json.keys():
		q = json[key][0]
		log_details['active_record_time'] = q[q.index("(") + 1:q.rindex(")")]  #find data btw "(" ,")""
		log_details['detail_422'] = q[q.index(": ") + 1:q.rindex("(")]
		q = json[key][1]
		log_details['time_stamp'] = q[q.index("[") + 1:q.rindex("]")]
		log_details['requested_url'] = q[q.index('"') + 1:q.rindex('"')]
		log_details['ip'] = q[q.index("r ") + 1:q.rindex(" a")]
		q = json[key][2]
		log_details['Processing_by_Spree'] = q[q.index(": ") + 1:]
		q = json[key][3] 
		log_details['parameters'] = q[q.index(":  ") + 1:]
		q = json[key][4]
		log_details['action_control'] = q[0]
		log_details['action_def'] = q[1:]
		full_details.append(log_details)

#def create_attachment():


def error(error_phrase):
				d = {}
				d_count = 0
				
				count  = -1
				for line in f:
					data = []
					action_data = []
					count = count + 1                   
					if  error_phrase in line:  #find line corresponding to given error phase
						pid = (f[count].split(" "))[2][1:-1]    #proccess id
						i = count
						data.append(f[i]) #append error line
						try:
								while(((LOG_Patterns.REQUEST_LINE.value)[loop_count] not in f[i]) or ((f[i].split(" "))[2][1:-1])!=pid):
												i = i -1   #goes upward till not find "Started GET" and "Started PATCH"

								data.append(f[i]),data.append(f[i+1]),data.append(f[i+2])  #append request line ,parameter line, processing line

								while(((LOG_Patterns.ACTION.value)[loop_count] not in f[i]) or ((f[i-1].split(" "))[2][1:-1])!=pid):
												i = i + 1  #goes downword till not find "ActionController"
								j = i

								while(f[j+1]!='\n' or f[j+2]!='\n'):   
												action_data.append(f[j]) #append ActioController data till it's next two lines are empty
												j = j + 1      
						except Exception as e:
								send_mail(e)								 
						data.append(action_data)
						d_count = d_count + 1
						d[d_count] = data
				return d		

for loop_count in range((LOG_Patterns.NO_OF_ERRORS.value)):
		full_details = []
		data = error((LOG_Patterns.ERROR_PHRASE.value)[loop_count])
		if(not data):
			send_mail("No error found")
		else:
			format_json(data)
			send_mail(full_details)

	
	