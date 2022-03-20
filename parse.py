import os
import re
from datetime import date
from tools import dir_mkr
from alive_progress import alive_bar
from datetime import datetime


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
	
	write_out_obj = open(write_out, "a")

	print("Parsing log data...")

	# # alive_progress.alive_bar
	
	# @2d0: for writing TRAFFIC-PER-IP sub-engine
	traffic_data = {}
	
	with alive_bar(len(read_lines), bar='bubbles', spinner='notes2') as bar:
		for e, line in enumerate(read_lines):
	
			# time.sleep(0.005)
			bar()
			
			try:
				ip = ip_re.search(line).group(1)
				data = ip_re.search(line).group(3)
				
				if ip in traffic_data.keys():
					traffic_data[ip].append(data)
				else:
					traffic_data[ip] = [data]
				
				# if ".js" in data or "email_blast" in data.lower():
				#     print("'.js' or 'email_blast' found for %s" % ip)
				
				write_out_obj.write("%s\n" % ip)
			
			except AttributeError as AErr:
				print("dbg|NO GROUP: %s" % line)
				continue
	
	write_out_obj.close()
	
	dump_ip_traffic(traffic_data, read_file)
	
	return write_out
	

def dump_ip_traffic(trf_dta: dict, file_given):
	# date string
	dt_string = datetime.now().strftime("%Y-%m-%d_%H%M")
	
	# full archive path
	save_path = os.path.join(os.getcwd(), "%s" % (dt_string))
	
	dir_mkr(save_path)
	
	dump_path = os.path.join(save_path, "TRAFFIC-PER-IP")
	# @2d0: integrate with archive function and place these files in that path instead
	dir_mkr(dump_path)
	
	for k, v in trf_dta.items():
		traffic_file_out = os.path.join(dump_path, "%s.txt" % k)
		traffic_out_obj = open(traffic_file_out, "a")
		
		for line in v:
			traffic_out_obj.write("%s\n" % line)
		
		traffic_out_obj.close()
	
	pass
	



if __name__ == "__main__":  # for testing specific input log
	in_file = "access_log"
	parser(in_file)











