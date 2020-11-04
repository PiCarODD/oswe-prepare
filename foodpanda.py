import requests
import string
import random
import json
url = "https://www.foodpanda.com.mm/api/v1/customers/email-check"
endpoints = ""
def checkacc():
	global email
	testemail = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))+"@gmail.com"
	url = "https://www.foodpanda.com.mm/api/v1/customers/email-check"
	data = {
	"email":testemail
	}
	headers = {
		'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
		'Content-Type': 'application/json;charset=utf-8',
		'Origin': 'https://www.foodpanda.com.mm',
		'X-Requested-With': 'XMLHttpRequest',
		'Accept': 'application/json'
		}
	cookie = {
		'Cookie': '__cfduid=d67fe2abdb69d96b294dc257a757600f71603707144; hl=en; AppVersion=d62170c; ld_key=65.18.124.72; perseusRolloutSplit=5; dhhPerseusGuestId=1603707124379.233342592473204540.7vb4rm1mht; _gcl_au=1.1.2013419955.1603707148; _pxvid=c03da180-1773-11eb-a0d7-0242ac120009; _tq_id.TV-81365445-1.6e06=47380cff0a918c26.1603707149.0.1603733433..; _ga=GA1.3.1705276839.1603707152; _gid=GA1.3.1249653340.1603707152; _fbp=fb.2.1603707158734.603492637; _pin_unauth=dWlkPU5UTXhabVpqTURrdE56VTNNaTAwT0RKbUxXRmpOR1F0TVdNME5qSXdOakptTkRkaQ; ab.storage.userId.c75f4e31-446b-411a-8b95-3e6897427041=%7B%22g%22%3A%22MM_684733%22%2C%22c%22%3A1603708954283%2C%22l%22%3A1603708954283%7D; ab.storage.sessionId.c75f4e31-446b-411a-8b95-3e6897427041=%7B%22g%22%3A%2205452161-a7a7-5385-3221-696c5fe3029a%22%2C%22e%22%3A1603713754778%2C%22c%22%3A1603711335894%2C%22l%22%3A1603711954778%7D; ab.storage.deviceId.c75f4e31-446b-411a-8b95-3e6897427041=%7B%22g%22%3A%2260af78e2-ab0c-7d4c-ce67-865f57cb9c5a%22%2C%22c%22%3A1603708954289%2C%22l%22%3A1603708954289%7D; tooltip-reorder=true; _px3=13ee046d0c257b9a7f5c8ffec195e1bae90b33e0665fd232f2d06b384e783f56:WWfkY7Opv793YndSP4TMn+HilXDYMstbA1B+wankOTY8xHl8MNWCWaw8bBQ2+ec12lDjmALJ+fZmjAmlut8IhQ==:1000:QfQcYw4Yf237CS2wn7aWqz+Wx06rH2BtYx6NeaT0T8fur8g+7r5g5YfVNvimr8qNgu+eRu45WoYLpsZm0gYMir8Y72H0KfgB5gxRMbVFB3wPIfScxRZZ5cshPJFKGTlwA9/pv14vOXqUQg1IUOh3JXZpYJQCrrSsBl5lLkFb1Ho=; dhhPerseusSessionId=1603733395089.783301884387080200.h80e37p8ohc; dhhPerseusHitId=1603733417535.259766599330869300.5ipkuemd1eg; _dc_gtm_UA-90537345-1=1; _gat_myTrackerDHH=1; _pxff_fp=1'
	}
	req = requests.post(url,json = data, headers = headers , cookies = cookie)
	resp = req.text
	if "this value should be valid email address" in resp or "\"has_password\":true" in resp:
		checkacc()
	else:
		return testemail
print(checkacc())