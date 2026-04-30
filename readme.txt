===========================================Project Format  Ist Stage    ======================================

StartUp/
 ├── app.py
 ├── requirements.txt  ← CLEAN (important)
 ├── runtime.txt


=========================================== project FOrmat Second Stage =======================================

StartUp/
│
├── main.py                  ← main entry
│
├── app/
│   ├── routes/
│   │   ├── web_routes.py
│
│   ├── views/
│   │   ├── templates/      ← HTML files yahan
│   │   │   ├── index.html
│   │   │   ├── user.html
│   │
│   ├── controllers/
│   ├── core/
│   ├── helpers/
│   ├── db/
│
├── requirements.txt
├── runtime.txt