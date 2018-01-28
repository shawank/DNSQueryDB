import time
import schedule
import dns
import csv
import argparse
import subprocess
import re
import json


def main():
	parser = argparse.ArgumentParser();
	parser.add_argument("mode", help = 'specify input means: interactive or file feed', type= str, choices = ['cli', 'file'], default = 'file')
	parser.add_argument("-f", "--filename", help = 'specify the file name in which you would like to store the data in case of file mode', type = str)
	parser.add_argument('-d', "domainname", help = 'specify the domain name in case of cli mode, skip  otherwise', type = str)
	args = parser.parse_args()
	if args.mode == "cli":
		if args.domainname:
			domainname = args.domainname.split(",")
		else:
			domainname = Input("Please input string of comma separated domain name")
		if args.filename:
			filename = args.filename
		else:
			filename = "dnsDB.csv"
		
		with open(filename, 'ab') as file:
			filewrite = csv.writer(file, quoting = csv.QUOTE_NONE, delimiter= ",")
			for dn in domainname:
				answer = dns_query(dn)
				filewrite.writerow(answer)

query(domainlist, storage_format, savefile)
	with open(domainlist, 'r+') as fr:
	    entriesTitle = ['Domain Name Returned', 'TTL', 'Unknown', 'Query Type', 'IP address']
	    output_file = savefile + storage_format
	    with open(output_file, 'w+') as fw:
	        if (storage_format == 'csv'):
	            writer = csv.writer(fw, quotechar='|', quoting=csv.QUOTE_MINIMAL)
	            
	            writer.writerow(['Domain Queried', 'Answer Type'] + entriesTitle)
	        domain = fr.readline()
	        j = 1
	        query_list = {}
	        while (domain):
	            temp = re.findall(r',([\w\.]+)', domain)
	            print(temp)
	            domain = temp[0]
	            result = subprocess.run(['dig', '+nocmd', '+noquestion', 'ANY', domain], stdout = subprocess.PIPE)
	            str = result.stdout.decode("UTF-8")
	            # pos_answer = findnth(str,"ANSWER", 1)
	            # # print(pos_answer)
	            # str_temp = str
	            # pos_authority = findnth(str, "AUTHORITY", 1, offset = 103)
	            # # print(pos_authority)
	            # pos_additional = findnth(str, "ADDITIONAL", 1, offset = pos_authority)
	            # # regex = re.compile(r'SECTION:\s+()')
	            match = re.findall(r'.+(?!SECTION)', str)
	            length = len(match)
	            i = 0
	            if (storage_format == 'csv'):
	                while (i < length):
	                    if (re.search(r':$', match[i])):
	                        temp = re.search(r'(\w+):$', match[i])
	                        if (temp.groups(1) == 'answer'):
	                            break
	                        element = re.findall(r'([\w\s]*):', match[i])
	                        answer_type = element[0]
	                        i += 1
	                        while(re.search(r'^[^;]', match[i]) != None):
	                            element = re.findall(r'([\w+\.:]+)\.?\t?', match[i])

	                            element = [j] + [domain] + [answer_type] + element
	                            writer.writerow(element)
	#                             json.dump(element, fw)
	                            i += 1
	                            if (i == length):
	                                break
	                        i -= 1

	                    i += 1
	            if (storage_format == 'json'):
	                
	                while (i < length):
	                    section_dict = {} 
	                    if (re.search(r':$', match[i])):
	                        temp = re.search(r'(\w+):$', match[i])
	                        if (temp.groups(1) == 'answer'):
	                            break
	                        element = re.findall(r'([\w\s]*):', match[i])
	                        answer_type = element[0]
	                        i += 1
	                        element_list = []
	                        while(re.search(r'^[^;]', match[i]) != None):
	                            element = re.findall(r'([\w+\.:]+)\.?\t?', match[i])
	    #                         writer.writerow(element)
	#                             json.dump(element, fw)
	                            element = dict(zip(entriesTitle, element))
	                            element_list.append(element)
	                            i += 1
	#                             if (i == length):
	#                                 break
	#                             section_list.a
	                        i -= 1
	                    section_dict[answer_type] = element_list
	                    query_list[domain] = section_dict
	                    i += 1
	                    
	            j += 1
	#             json.dump({domain: section_dict}, fw)
	            
	            domain = fr.readline()
	        if (storage_format == 'json'):
	            json.dump(query_list, fw)


if __name__ == "__main__"
	main()



