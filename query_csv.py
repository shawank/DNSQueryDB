import csv
import subprocess
import re

with open('domainlist.csv', 'r+') as fr:
    with open('database2.csv', 'w+') as fw:
        domain = fr.readline()
        writer = csv.writer(fw, quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Domain Queried', 'Answer Type', 'Domain Name Returned', 'TTL', 'Unknown', 'Query Type', 'IP address'])
        j = 1
        while (domain):
            temp = re.findall(r',([\w\.]+)', domain)
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
                        i += 1
                        if (i == length):
                            break
                    i -= 1

                i += 1
            j += 1
            domain = fr.readline()
