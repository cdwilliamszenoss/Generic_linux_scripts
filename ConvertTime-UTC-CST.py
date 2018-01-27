#!/usr/bin/python

import time 
import re

def main():
 print "\n## Caculate IM Minutes ##\n"
 result = get_start_end_time()
 print "\n"

 fault_time_secs = result["fault_time"]
 restore_time_secs = result["restore_time"]
 
 IM_result = calculate_time_differences(fault_time_secs,restore_time_secs)
 
 if IM_result["total_IM_mins"] < 0 :
  print "\n****** Incorrect Time ******\n"
  print "\nCheck input times.\n" 
 else:
  print "\n****** Results ******\n"
  print "\n\nTotal time in  minutes: %d" % IM_result["total_IM_mins"]
  print "Total time in hours and minutes: %d hrs %d mins\n" %(IM_result["hours"], IM_result["minutes"])

# Main Ends

def get_start_end_time():
 print ("**** Enter Time Fault Occured ****\n")
 
 today = time.strftime("%-d/%b/%y %I:%-M %p")
 print "Current datetime: " + today 
 while True:
  get_fault_date_time = raw_input("Enter Fault date and time: ").strip()
  if not re.search(r"([0-9]{1,2})\/([A-Z].{1,2})\/([0-9]{1,2})\s([0-9]{1,2})\:([0-9]{1,2})\s((?:a|p)m)", get_fault_date_time,re.I):
   print "Use correct format:"
   continue
  else:
   break

 fault = re.search(r"([0-9]{1,2})\/([A-Z].{1,2})\/([0-9]{1,2})\s([0-9]{1,2})\:([0-9]{1,2})\s((?:a|p)m)", get_fault_date_time,re.I)
 fault_groups = fault.group(1)+" " + fault.group(2)+" " + fault.group(3)+" " + fault.group(4)+" " + fault.group(5)+ " " + fault.group(6)
 fault_time = time.mktime(time.strptime(fault_groups,"%d %b %y %I %M %p"))


 print ("\n**** Enter Restored Time ****\n")
 while True:
  get_restore_date_time = raw_input("Enter Restored date and time: ")
  if not re.search(r"([0-9]{1,2})\/([A-Z].{1,2})\/([0-9]{1,2})\s([0-9]{1,2})\:([0-9]{1,2})\s((?:a|p)m)", get_restore_date_time,re.I):
   print "Use correct format:"
   continue
  else:
   break
  
 restore = re.search(r"([0-9]{1,2})\/([A-Z].{1,2})\/([0-9]{1,2})\s([0-9]{1,2})\:([0-9]{1,2})\s((?:a|p)m)", get_restore_date_time,re.I)
 restore_groups = restore.group(1)+" " + restore.group(2)+" " + restore.group(3)+" " + restore.group(4)+" " + restore.group(5)+ " " + restore.group(6)
 restore_time = time.mktime(time.strptime(restore_groups,"%d %b %y %I %M %p"))

 return {"fault_time":fault_time,"restore_time":restore_time}




def calculate_time_differences(fault_time_secs,restore_time_secs):
  
  date_time_format_output = "%-d/%b/%y %I:%M %p"
  cdt_fault_localtime = time.strftime(date_time_format_output,time.localtime(fault_time_secs))
  utc_fault_gmtime = time.strftime(date_time_format_output,time.gmtime(fault_time_secs))

  cdt_restore_localtime = time.strftime(date_time_format_output,time.localtime(restore_time_secs))
  utc_restore_gmtime = time.strftime(date_time_format_output,time.gmtime(restore_time_secs))
 
  print "\n************ IM Start Time **********\n"
  if cdt_fault_localtime in utc_fault_gmtime:
    print "Server is set to UTC time."
    print "Date UTC:  %s " %(utc_fault_gmtime)
  else:
    print "Date CDT: %s\n" %(cdt_fault_localtime)
    print "Date UTC:  %s " %(utc_fault_gmtime)


  print "\n************ IM Service Restored Time **********\n"
  if cdt_restore_localtime in utc_restore_gmtime:
   print "Server is set to UTC time."
   print "Date UTC: %s " %(utc_restore_gmtime)
  else:
   print "Date CDT: %s\n" %(cdt_restore_localtime)
   print "Date UTC: %s " %(utc_restore_gmtime)

  total_IM_mins = (restore_time_secs - fault_time_secs) / 60
  hours = total_IM_mins / 60
  minutes = total_IM_mins % 60

  return {"total_IM_mins":total_IM_mins,"hours":hours,"minutes":minutes}



#### Calling main program 
 

if __name__ == '__main__':
 main()
