import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc = {
"name": "陳羿光",
"nick name": "地瓜球"
}

doc_ref = db.collection("PU123").document("7VfXPXreMVH7OcOShsTq")
doc_ref.set(doc)