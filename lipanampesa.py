#print ("Welcome to full stack Django");
#from oauthlib.oauth2 import BackendApplicationClient
#from requests.auth import HTTPBasicAuth
#from requests_oauthlib import OAuth2Session

import requests;
import posts;
import keys;
from datetime import datetime;
import base64;
import json;
from requests.auth import HTTPBasicAuth;

unformated_time=datetime.now()
formated_time=unformated_time.strftime("%Y%m%d%H%M%S");
print(formated_time);

data_to_endode = keys.businessShortCode + keys.lipa_na_mpesa_passkey + formated_time
encodedstr = base64.b64encode(data_to_endode.encode())
print(encodedstr);

decoded_password = encodedstr.decode('utf-8')

print(decoded_password)


consumer_key = keys.consumer_key
consumer_secrtet = keys.consumer_secret
apiurl = keys.url

r = requests.get(apiurl,auth=HTTPBasicAuth(consumer_key,consumer_secrtet))


access_token = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers = { 'Authorization': 'Basic R1phdDBXV29VcWhTZWd2Zk43TDBFZXoyWlQwejBiQmVsN1V2bkxDNllkaWJUd0hBOkE2ZzFOclFBNlByMTFYa1gwS2Qyc05JUVlLYVhnb1B6emhXSnB5NnpwZ0d3WjJaM0NJRnNUajFob1F2SnJhdnI=' })
tokens = json.loads(access_token.text.encode('utf8'))
access_token1=tokens['access_token']
print(access_token1)


json_response=access_token.json()



my_json_token = json_response['access_token']
print(my_json_token + " edited json token")
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest";
headers =  {"Authorization": "Bearer %s" % my_json_token}

def lipa_na_mpesa():
 request = {    
   "BusinessShortCode": keys.businessShortCode,    
   "Password": decoded_password,    
   "Timestamp": formated_time,    
   "TransactionType": "CustomerPayBillOnline",   
       "Amount": 1, 
    "PartyA": keys.phonenumber,
    "PartyB": keys.businessShortCode,
    "PhoneNumber": keys.phonenumber,   
   "CallBackURL": "https://mydomain.com/pat",    
   "AccountReference":"CompanyXLTD",    
  "TransactionDesc":"Payment of school fees"
    };

 response = requests.post(api_url,json=request, headers=headers);
 print (response.text);

 print ("the whole resp:");
 print (r.text);
lipa_na_mpesa();