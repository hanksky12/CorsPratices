# 介紹
docker 包含
nginx(原站前端)
backend(原站後端)

本地
backend_cors(跨域站的後端)


# 請求流程:
第一步：
從browser 像docker-nginx送請求，拿到首頁
並用js fetch 讓docker-nginx轉發到docker-backend 設定cookie

第二步：
主動用js fetch 向本地後端送cors請求，遇到問題

# 目前問題點:
cors的delete請求已成功做到跨域拿到返回的資料，但這個請求無法讓browser帶上cookie

## 已知設定:
### 原站設定的cookie

secure=True
samesite='None'
httponly=False

### 前端fetch

credentials: 'include'
無任何額外header

### 跨站的後端

網站已掛https

response.headers["Access-Control-Allow-Origin"] = "http://localhost"

response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"

response.headers["Access-Control-Allow-Credentials"] = "true"

## 已嘗試還是失敗的部分:

前端改用axios
前端fetc多加 mode:cors
後端用cors套件
跨域先用get嘗試


#如要拉專案下來測試：
還需要自簽ssl，讓跨站後端可運行在https

