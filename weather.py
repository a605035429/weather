import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#資料庫金鑰
cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "weather-api-aad1d",
  "private_key_id": "90d6c60b1ebabc8ccbb03f2547d3d191646917ae",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDovnHQqx0N8cnu\nraI3nbwgMxJlrWRIsCd+xzhQQMq0uKvd5DyEz6TdLH0L2TJ7//CVE1aOoaL26GuO\nAS42sGxajWPbK/I+ouk02s6rNesEqEZWOy8D1rJImjd1JYRdJsdI7L7BJpMORL2e\nXRXFS+jP39KUJQTBWarlHI+18mm/9Hoh+p2E/nVeemZKszwcfoIQ0OsQSlFqFcrZ\nIiEDOWXJtjbsLRQovfmZjGQloMJklNR5yeksEa9UPSrqclLoYE4H5UFBLKj41AXt\nZSwAP1//Lth2j19SCrD/pT+zXyQyQssuYLB1/Wb1w7x+SN4V4HUDHwsHihN18bpi\nEmgh88qlAgMBAAECggEAGnLV7UAcv6Jr76ckqYxPvhr/qrVPEaGPA22xPRF315yq\nzz7qD6+nDQlKtod6oLO/i7lUW0YMBmH4Iv2IWmenEI1DvTrbvvl1Ze+9j6BDclaL\nE66LE7UYsn5v8eyPA6Tt/aAFt15iVLtEDxSF7lNHhCPrwrEIPs6pSHr769G96bWv\nkgUI3cYMvn4AT2TBaRICYS6wVlD6r+DX92flB/BqjvC8FYBvHAPdVgwvy+x+y8lu\nCgvpNS1/oMony5LC7pK4gWJo4x1+Ly/JgRZY3SQNDqdnWCtbz9P289n/Aq0X8Pah\nxBLeEgkWB+GqgQf8yAdB6syYsh4o59JabqONldLq4QKBgQD6rFcnV8Y2cHJWWT77\nwW4vhAcAKU9VnwevoD8VQY+HLbkkXz1299HPufzTM6qeQhz7CNduW8dNmgi+wRLf\n9aRBblogKHYzwzfc3dD+xlXkRzAwrkXG78tA8R7J8vSKBVQwLHMyY6rfF8t4y8ni\nF99dY/3JTYdzWlKxUPr+9uXkUQKBgQDtsJGtUa0ZdfRxCTiwJVKmEnMSNW2WEYDi\n5FTt0o9m1pYJJCETBtmFVATbAAKps73tOWaNRPdBSR81+vu2e0M9QKNe6s94xzOs\nmNs2TSWutJfTZoD46qa9LlcQIuTq/JmKDdnTW09iG8AMvmPEQRnTgfaQgRvw542Q\nkbO8X+MQFQKBgQCb326SWFI4p9NxPi2b/ru1cDOqNgXPCASPgOW5IftN43Cs3Uwr\nHg6pTM2ZxxbhMdszflv3k7pq1s15UDWcbfKlfSkttftKVKn3/TZoNoxSVrHwk21w\nNsv8pfKvQRQufwHKstkvDCrEbtdnVdFDdfS+7d5xvnPrls6009Y/lOd/AQKBgE0I\nhK4fYnJ2ABsCWhT8g6S/JfwoxLN2SMdAKSZKr58svMOJqg54kdbcPBaeEj7duhhA\nGjR+vYOzJyJfjWS+3jPj1w7UGxmRtfWiNKmMp0HP1cT126bQpel6M01PgdGGvFw5\n0PbnCPtK8xsuOTdJwg0Ced6reVrCMOdB0XajvPthAoGAA6a12jniSowoqUiD566y\nWpVJfo44VzNzYZPLCXYHhaT8f8hThMGD5m1anjdaItHNTbsJfd1W9KHuPwCfp/my\n2jObM5EPTt/LiRwJbZ5KM8yuaz+624ei417i659VH7E+yEX9xDXAhNqu2WGjceOd\n6pTNzwKZnyQpzwQWUl4xSYA=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-cp94q@weather-api-aad1d.iam.gserviceaccount.com",
  "client_id": "104233028598558085617",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-cp94q%40weather-api-aad1d.iam.gserviceaccount.com"
})
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


            

