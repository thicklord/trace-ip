import ipinfo
import pathlib2
import json
import progressbar
import time
import os, shutil
from datetime import date
import unicodedata, unidecode
from alive_progress import alive_bar



def trace_ip(file_in):
    # API info for IPINFO
    api_key = "a89a6ebe9f9d1f"
    # IPINFO handler object
    ip_handler = ipinfo.getHandler(api_key)
    
    ips_quantified = file_in
    
    results_file = file_in.replace("quantified", "results")
    
    
    
    with open(ips_quantified, "r") as irdr:
        data = dict(json.loads(irdr.read()))
       
    # remove existing results file
    if os.path.exists(results_file):
        os.remove(results_file)
    
    iwrt = open(results_file, "w")
    
    # list for output dump of IP data
    data_by_ip_list = []
    
    print("Retrieving data via IP lookup...")
    
    with alive_bar(len(data), bar='filling', spinner='waves') as bar:
        # iterate over 'data': k=IP address and v=access_attempts
        for k, v in data.items():
            # retrieve details from IPINFO with IP as the argument
            details = ip_handler.getDetails(k)
            
            # time.sleep(.0005)
            bar()
            
            # build data dictionary for clean JSON formatting later, include all details from IPINFO API dump
            data[k] = {
                "access_attempts": v,
                "details": details.all
            }
            
            # decode all data for IP data in dictionary
            for d, dv in data[k]['details'].items():
                data[k]['details'][d] = unidecode.unidecode(u'%s' % dv)
                
            try:
                # # debug test line: print all details for all originating IP outside US
                # if details.country != "US":
                #     print(k, data[k], sep=": ")
                
                # append data to working output list
                data_by_ip_list.append({k: data[k]})
            
            except AttributeError as AE:
                # # //db&t
                # print("no country")
                # print(details.all)
                # # //db&t
                
                data_by_ip_list.append({k: data[k]})
                continue
        
    json.dump(data_by_ip_list, iwrt, indent=4)
    
    # writer close for appending to file
    iwrt.close()
    
    return results_file

# # batch write
# with open(results_file, "w") as iwrt:
#     json.dump(data, iwrt)


if __name__ == "__main__":
    file_quantified = str("2020-12-15_www.dhpsupply.com-access_log_IPs-quantified.json")
    trace_ip(file_quantified)











