import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#資料庫金鑰
cred = credentials.Certificate('firebasekey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
#創建資料庫
doc_ref = db.collection("weather").document("list")
#台灣各個縣市代號

for i in range (1,22):
    x=['F-D0047-001','F-D0047-005','F-D0047-009','F-D0047-013','F-D0047-017','F-D0047-021','F-D0047-025','F-D0047-029','F-D0047-033','F-D0047-037','F-D0047-041','F-D0047-045','F-D0047-049','F-D0047-053','F-D0047-057','F-D0047-061','F-D0047-065','F-D0047-069','F-D0047-073','F-D0047-077','F-D0047-081','F-D0047-085']
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/"+x[i]+"?Authorization=CWB-50D0DBCE-C45E-4042-9DD7-0B62BC13BABC&format=JSON"
    data = requests.get(url)
    data_json = data.json()
    #print(data_json)
    doc_ref.set(data_json)


            

