import os,datetime
from helpers import LOG_keywords
file_path_1 = LOG_keywords.LOG_FILE_LOCATION.value  #file_location_of_log_file
i = datetime.datetime.now().isoformat()
os.system("mkdir " + LOG_keywords.LOG_DIRECTORY.value + (i.split("T"))[0])
os.system("touch "+ LOG_keywords.LOG_DIRECTORY.value + (i.split("T"))[0] + "/" + ((i.split("T"))[1])[:2] + ".log")  #create file and name its as present timestamp
os.system("cp "+ file_path_1 + " " + LOG_keywords.LOG_DIRECTORY.value + (i.split("T"))[0] + "/" + ((i.split("T"))[1])[:2] + ".log" )     
os.system(">" + LOG_keywords.LOG_FILE_LOCATION.value)   #make the file empty
