import sys,json, requests
PROTOCOL = 'http'
PORT = '8080'

SERVER = sys.argv[1]
USER = sys.argv[2]
PASS = sys.argv[3]
FILE = sys.argv[4]

BASE_URL = PROTOCOL + '://' + SERVER + ':' + PORT + '/rest' 
s = requests.Session() 
# LOGIN 
url = BASE_URL + '/client/login' 
headers = {'Accept': 'application/json' , 'Content-Type': 'application/json; charset=UTF-8'} 
payload = {'name': USER , 'password': PASS , 'accountName': 'default'} 
response = s.post(url, headers=headers, data=json.dumps(payload)) 
print ("Connect: ", response.status_code)

hp4msecret = response.headers['x-hp4msecret']
jsession = s.cookies['JSESSIONID']


if response.status_code == requests.codes.ok: 
# UPLOAD APP 
    url = BASE_URL + '/apps' 
    file = {'fileUpload': open(FILE, 'rb')} 
    headers = {'x-hp4msecret': hp4msecret, 'JSESSIONID': jsession} 
    response = s.post(url, headers=headers, files=file) 
    print ("Upload: ", response.status_code) 

if response.status_code == requests.codes.ok: 
    print ("App Name:", response.json()["name"]) 
    print ("App Id:", response.json()["id"]) 
    print ("App version:", response.json()["version"]) 
    #print ("App Count:", response.json()["count"]) 
