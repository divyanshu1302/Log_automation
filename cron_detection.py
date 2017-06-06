from pyexcel_ods import get_data
import json
from helpers import Cron_keywords
import pdb
from email.mime.text import MIMEText as text
import smtplib

def send_mail(l):      #fucntion for sending mail
		TEXT = "\n\n"
		for i in range(len(l)):
				TEXT = TEXT + """
				TASK-NAME: %s
				HOUR: %s
				MINUTES: %s	
				""" % (l[i][0],l[i][1],l[i][2])
		# Prepare actual message
		m = text(TEXT)

		m['Subject'] = Cron_keywords.MAIL_SUBJECT.value
		m['From'] = Cron_keywords.MAIL_FROM.value
		m['To'] = Cron_keywords.MAIL_TO.value
		server = smtplib.SMTP(host='smtp.gmail.com', port=587)
		server.starttls()
		server.login(Cron_keywords.MAIL_FROM.value, Cron_keywords.MAIL_PASSWORD.value)
		server.sendmail(m['From'], m['To'], m.as_string())
		server.quit()


data = get_data(Cron_keywords.ods_file_path.value)
# first_row = ['task name', 'task freq.', 'hour', 'minute']
# f_index = {}
a = json.dumps(data) #json in string form
b = json.loads(a)  #json in dict form
p = b[Cron_keywords.sheet_name.value]   #present sheet
send_list = [] 

# pdb.set_trace()
# for w in first_row:
# 	f_index[w] = p[0].index(w)

with open(Cron_keywords.log_file_path.value) as f:
	f = f.readlines()
time_list = {}


for j in range(1,len(p)):	        #this loop will make dictionary with time as its indexes and values as list of cron tasks at that particular index
				time_task = []
				for i in range(len(f)):
					time = ((f[i].split(" "))[2]).split(":")   #extract time from logs	
					if((int(time[0]) == p[j][2]) and (int(time[1]) == p[j][3]) and ("CRON" in f[i])):   #find till it find out particluar task at given time
						while((int(time[0]) == p[j][2]) and (int(time[1]) == p[j][3]) and ("CRON" in f[i])):
							time_task.append(f[i])
							i = i + 1	
						break	
				time_list[(p[j][2])*60 + p[j][3]] = time_task

# print time_list[420]
for k in range(1,len(p)):        #search for particular task at particular time by using time as index
			h = p[k][2]
			m = p[k][3]
			count = 0
			if (time_list[(p[k][2])*60 + p[k][3]] != []):
				for line in time_list[(p[k][2])*60 + p[k][3]]:
					if(p[k][0] in line):
						count  = count + 1
				if(count==0):	
					send_list.append([p[k][0],p[k][2],p[k][3]])
			else:
				send_list.append([p[k][0],p[k][2],p[k][3]])   #this list will contains all non working cron tasks
# print send_list	

send_mail(send_list)
