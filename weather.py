import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#資料庫金鑰
cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "weather-api-aad1d",
  "private_key_id": "830d55fa9efa92e4a83c08f33807251a4a281924",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDN/b7/KZgMzFg1\nEyaKqqP2C+v6TTrTlZdXgHoPrVUuY65hjpUXPhx+7J5Qf28/lB0yKtffTQM1NNH+\n8alll9MykE2hUaeZAxlfSMgdMQHUW84h4GErGDxnzv4hc1gWsk/0d5ChhcIzk/H9\nVhP3mlBLg9UCrV8SWopeRpw5pOUAuQosnLGDQK1Iypyv3OYQX7fo5Ws7XwrnseVY\ne3AOel+fIgYhiT4MJWI4muugFLJDzWG7ynRcxPy8fkbWROwNQYfcRrcT1gvhNIAJ\nQqb9B2AvAdQPbU/3kWnRyp9rthOnqTQ3rbEYeyJel/hGujdu/XCPtvktJ0SAgab/\nmFUgGKLrAgMBAAECggEAUS3cbQuT0AtiAbyj1kcMacVmAJUaB1NvOr03nWEGbks7\naFf8GpZQPZb7hybJjWlOHjyzKV3c00WXMp1DUHXGdilXZqla3trRT3NL5fEv0uRB\nNqmKMaUR/Skejsk5oGwyRVovZfBkSdZWqiuXn98xIKl6M11m18FVwXSbUb5Rv3f2\n94IDxT9dyTD6xbL/JWXkGmFo3heSYqtDJBRiu88a/g2wd6gL5j/20t0t9e8zCm5D\nXbuOeoXA82/zNtIqlw1o7HY/meuR4MoYyfNvf0IBROQXWR1hA4spyLYgejyp0Kpz\nFGVBX2XCAR21NwB4hwiqY7EJ7vbWh/FTgEINJYk7DQKBgQD+zOqTQ4fTJqHc1GQu\nKVyPkOsYC5l+LR8zHmeiqNYr4X8eP5EeIvyFUXH8pgEi3RPCQnzqaOjSrj/LGXbn\nQfPDP2Dzxw+sf3i+ftqN04aw8Inj0DeKGV/ALhcUQnYJiDtr2KQWfHmQ4hMZzy1F\n3K18u49opI4q6JTDjeOc2dXiJwKBgQDO9gFU2JojwjG/9GR0ekX2wbF4S/tJkrxO\n7QgiBeYbwJppPBaWn3N1kWgsWvLs6LO1IaSGFMj8KBhnvM+XNLJ6cDZ/8RpUGTQG\nw9bJAKaT2Tg8tx4AvE7wb8JCy6uc8JPaGGRYSYmmZFJqAT67vq0XLRCtPlDCBhuM\nooB0il8nnQKBgDMHTO9DNf92nDICozGPfQcPidWd9RaM6NOvAihUUdgl5/Rh3KlB\nbnswrXhgspeN2PgtoqC7c+1FkmcVaXe1AKGYns0Tj7MHMGJOO2zt8OqcsbDbMVRJ\n8qAlWt/m04bjLqtRjsMmGJ6IeDTSBgoYwPHbCkR1uDclry1ezDfMdIY/AoGBAIKY\nk9CBegq0gQY65qTlf36tTRq2/5O2p2M6iZZGmKTMjeN4ClzzszzuC4lpvr8mPDhB\nSXteZFFRz8yuRWSJ2VIPuyRS9SU6Xi0iqUdfRL4pJSaS+rjGGx33t+LEeL9oxDOs\njq1zggvgZG0F6hs4wCrOwiZAG1/D0OCWrm5b3p21AoGAImQnTmmhCe0HZuHBUv2d\nS4NC/C4A2o6zxbP+pEQw+n4gIo4b6IuWlS4Lqi6ht+/X/Xq4vVIglm9vbaCmczQB\n4sHzs0Tc88NG6Rn+ybU/ufAbUzpcdrdR31IVF944AL3r8WopCEE8eV0HfowCuNaj\no4CgcJ+xRdeG0m6JPmmHCCM=\n-----END PRIVATE KEY-----\n",
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


            

