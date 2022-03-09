import os
import re
from datetime import date

from alive_progress import alive_bar


def parser(read_file):
	# function for parsing apache log data for captured IPs
	
	if not os.path.exists(read_file):
		print("File not found: '%s'; stopping parse..." % read_file)
		quit()
	
	with open(read_file, "r") as rdr:
		read_lines = rdr.readlines()
	
	# build IP address regular expression
	ip_re = re.compile(r"(\d+\.\d+\.\d+\.\d+) (- -)?(.*)")
	
	# specify output file of captured IPs
	write_out = "%s_%s_IPs.txt" % (date.today(), read_file)
	
	wobj = open(write_out, "a")

	print("Parsing log data...")

	# # alive_progress.alive_bar
	with alive_bar(len(read_lines), bar='bubbles', spinner='notes2') as bar:
		for e, line in enumerate(read_lines):
	
			# time.sleep(0.005)
			bar()
			
			try:
				ip = ip_re.search(line).group(1)
				data = ip_re.search(line).group(3)
				
				# if ".js" in data or "email_blast" in data.lower():
				#     print("'.js' or 'email_blast' found for %s" % ip)
				
				wobj.write("%s\n" % ip)
			
			except AttributeError as AErr:
				print("dbg|NO GROUP: %s" % line)
				continue
	
	wobj.close()
	
	return write_out
	



if __name__ == "__main__":  # for testing specific input log
	in_file = "access_log"
	parser(in_file)











