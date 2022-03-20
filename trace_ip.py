import json
import os
import ipinfo
import pandas as pd
import pathlib2
import unidecode
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
            
            # # build data dictionary for clean JSON formatting later, include all details from IPINFO API dump
            tmp_dct = {
                "IP_address": k,
                "access_attempts": v,
                "details": details.all
            }
            
            # decode all data for IP data in dictionary
            for d, dv in tmp_dct['details'].items():
                tmp_dct['details'][d] = unidecode.unidecode(u'%s' % dv)

            data_by_ip_list.append(tmp_dct)
            
            del tmp_dct
            
    json.dump(data_by_ip_list, iwrt, indent=4)
    
    # writer close for appending to file
    iwrt.close()
    
    return results_file

# # batch write
# with open(results_file, "w") as iwrt:
#     json.dump(data, iwrt)


def json_to_excel(json_file):
    
    # still working out bugs with formatting of JSON conversion
    file_name = pathlib2.Path(json_file).name
    file_name = file_name.replace('json', 'xlsx')
    
    print(file_name)

    xlsx_out = os.path.join(pathlib2.Path(json_file).parent, file_name)
    
    try:

        df_json = pd.read_json(json_file)

        df_json.to_excel(xlsx_out)

        print("converted JSON to excel file: %s" % xlsx_out)

    except Exception as EX:
        print("error converting JSON to xlsx: %s" % str(EX))

    
    
    
    
    pass


if __name__ == "__main__":
    
    json_to_excel("2022-03-08_access_log_merged_IPs-results.json")
    











