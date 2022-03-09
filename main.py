from parse import parser
from trace_ip import trace_ip, json_to_excel
from quantify_ips import quantify
from pathlib2 import Path
import sys
import os
import shutil
from tools import archive_temp_files


if len(sys.argv) > 1:
	# command line input
	in_file = Path(sys.argv[1])
	
	local_file = os.path.join(os.path.abspath(in_file))

else:
	# # wrapper script only works if the file is in the script directory
	in_file = "company2-access_log_2021-08-24"

	local_file = os.path.join(os.getcwd(), in_file)
#
# if in_file != local_file:
#     shutil.copyfile(in_file, local_file)
# else:
#     local_file = in_file

# for shorthand file path
local_file = os.path.basename(local_file)

# parse IPs
parsed_results = parser(local_file)

# quantify IPs
quantified_file = quantify(parsed_results)

# IP trace with geolocation dump to JSON
results_file = trace_ip(quantified_file)

print(results_file)

# archive_temp_files([local_file, parsed_results, quantified_file])

















