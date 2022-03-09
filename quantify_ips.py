import os

import simplejson as json


def quantify(in_file, minimum_attempts=200):
    # function to calculate the number of times an IP address appears in the log, then trims the dictionary based on minimum number of attempts to filter for
    # Set 'minimum_attempts=None' if this needs to be bypassed
    ip_quant_dict = {}
    
    parsed_infile = in_file
    
    pfilename_split = list(os.path.splitext(parsed_infile))

    with open(parsed_infile, 'r') as rdr:
        
        print("Quantifying parsed IPs...")
        
        for l in rdr.readlines():
            d = l.split('\n')[0]
            
            if d in ip_quant_dict.keys():
                ip_quant_dict[d] += 1
            
            else:
                ip_quant_dict[d] = 1
                
    ip_quant_dict = sorted(ip_quant_dict.items(), key=lambda x: x[1], reverse=True)
    
    filtered_list = []
    
    # minimum_attempts refers to the amount of occurrences by IP, when minimum_attempts=200 (default) IP's with access attempts of 200 or greater will be kept in the results. This value can be set to 'None' to keep all access attempts
    # minimum_attempts also keeps the number of API calls to only relevant/suspected IP addresses
    if minimum_attempts:
        for d in ip_quant_dict:
            if int(d[1]) >= minimum_attempts:
                filtered_list.append((d[0], d[1]))
    else:
        filtered_list = ip_quant_dict
    
    # set out-file to json output
    write_file = "%s-quantified.json" % pfilename_split[0]
    
    with open(write_file, 'w') as wrt:
        json.dump(filtered_list, wrt, indent=4)
    
    return write_file


if __name__ == "__main__":
    # # //db&t
    # parsed_file = "2022-02-27_company1-access_log_IPs.txt"
    # quantify(parsed_file)
    # # //db&t
    
    pass

