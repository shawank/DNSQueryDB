import dns
import csv
import argparse
import subprocess
def dnsquery(dn):
	result = subprocess.run(['dig', dn], stdout = subprocess.PIPE)
	return result.stdout.decode("UTF-8")

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


if __name__ == "__main__"
	main()