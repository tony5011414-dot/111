# 任務管理系統 (Task Management System)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18+-61dafb.svg)](https://react.dev/)
[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)

一個基於 React 前端和 Django 後端的全端任務管理系統，幫助使用者有效管理日常任務，提升工作效率。

## 📋 目錄

- [功能特色](#-功能特色)
- [技術棧](#-技術棧)
- [快速開始](#-快速開始)
- [專案結構](#-專案結構)
- [API 文件](#-api-文件)
- [開發指南](#-開發指南)
- [部署](#-部署)
- [貢獻](#-貢獻)
- [授權](#-授權)

## ✨ 功能特色

- 🔐 **使用者認證**：JWT Token 認證機制，安全的用戶登入與註冊
- 📝 **任務管理**：完整的 CRUD 操作，建立、編輯、刪除任務
- 🏷️ **分類與標籤**：靈活的任務組織方式，支援自訂分類
- 🔍 **搜尋與篩選**：快速找到需要的任務，支援多條件組合查詢
- ⏰ **時間管理**：截止日期提醒與任務統計
- 📊 **資料統計**：任務完成率與趨勢分析（進階功能）
- 🎨 **現代化 UI**：響應式設計，支援多種裝置

## 🛠️ 技術棧

### 前端

- **React 18+** - 現代化的前端框架
- **React Router** - 單頁應用路由管理
- **Axios** - HTTP 請求處理
- **Context API** - 狀態管理
- **Material-UI / Ant Design** - UI 元件庫（可選）

### 後端

- **Django 4.2** - Python Web 框架
- **Django REST Framework** - RESTful API 開發
- **PostgreSQL** - 關聯式資料庫
- **JWT Authentication** - Token 認證機制
- **Django Filter** - 進階過濾功能

### 部署

- **Docker** - 應用程式容器化
- **Docker Compose** - 多容器應用編排
- **Nginx** - 反向代理與靜態檔案服務

## 🚀 快速開始

### 前置需求

- Python 3.11+
- Node.js 18+
- Docker & Docker Compose（可選，推薦使用）

### 方法一：使用 Docker 部署（推薦）

這是最簡單的部署方式，適合快速體驗專案。

```bash
# 1. 複製專案
git clone https://github.com/你的使用者名稱/task-management-system.git
cd task-management-system

# 2. 設定環境變數
cp .env.example .env
# 編輯 .env 檔案，設定你的配置（至少修改 SECRET_KEY 和 DB_PASSWORD）

# 3. 啟動所有服務
docker-compose up -d

# 4. 執行資料庫遷移
docker-compose exec backend python manage.py migrate

# 5. 建立超級用戶（可選，用於管理後台）
docker-compose exec backend python manage.py createsuperuser
```

訪問應用：

- 🌐 **前端應用**：http://localhost:3000
- 🔌 **後端 API**：http://localhost:8000/api
- ⚙️ **管理後台**：http://localhost:8000/admin

停止服務：

```bash
docker-compose down
```

### 方法二：本地開發

適合需要修改程式碼的開發環境。

#### 後端設定

```bash
cd backend

# 建立虛擬環境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安裝依賴
pip install -r requirements.txt

# 設定環境變數
cp .env.example .env
# 編輯 .env 檔案

# 執行資料庫遷移
python manage.py migrate

# 建立超級用戶
python manage.py createsuperuser

# 啟動開發伺服器
python manage.py runserver
```

後端將運行在 http://localhost:8000

#### 前端設定

```bash
cd frontend

# 安裝依賴
npm install

# 設定環境變數
# 建立 .env 檔案，設定 REACT_APP_API_URL=http://localhost:8000

# 啟動開發伺服器
npm start
```

前端將運行在 http://localhost:3000

## 📁 專案結構

```
task-management-system/
├── backend/                    # Django 後端專案
│   ├── manage.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── backend/               # Django 專案設定
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── accounts/              # 用戶認證應用
│   ├── tasks/                 # 任務管理應用
│   └── categories/            # 分類管理應用
│
├── frontend/                   # React 前端專案
│   ├── package.json
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── public/
│   └── src/
│       ├── components/        # React 元件
│       ├── pages/             # 頁面元件
│       ├── services/          # API 服務
│       ├── context/           # Context API
│       └── utils/             # 工具函數
│
├── docker-compose.yml         # Docker Compose 設定
├── .env.example               # 環境變數範例
├── README.md                  # 專案說明（本檔案）
└── 專案說明文件.md            # 詳細開發文件
```

## 📖 API 文件

### 認證端點

- `POST /api/auth/register/` - 用戶註冊
- `POST /api/auth/login/` - 用戶登入
- `POST /api/auth/refresh/` - 刷新 Token
- `POST /api/auth/logout/` - 用戶登出

### 任務端點

- `GET /api/tasks/` - 獲取任務列表（支援篩選、搜尋、排序）
- `POST /api/tasks/` - 建立新任務
- `GET /api/tasks/{id}/` - 獲取任務詳情
- `PUT /api/tasks/{id}/` - 更新任務
- `PATCH /api/tasks/{id}/` - 部分更新任務
- `DELETE /api/tasks/{id}/` - 刪除任務

### 分類端點

- `GET /api/categories/` - 獲取分類列表
- `POST /api/categories/` - 建立新分類
- `GET /api/categories/{id}/` - 獲取分類詳情
- `PUT /api/categories/{id}/` - 更新分類
- `DELETE /api/categories/{id}/` - 刪除分類

**注意**：所有 API 端點（除認證外）都需要 JWT Token 認證。

## 🛠️ 開發指南

### 環境變數設定

複製 `.env.example` 並重新命名為 `.env`，然後修改以下變數：

```env
# Django 設定
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# 資料庫設定
DB_NAME=taskdb
DB_USER=postgres
DB_PASSWORD=your-database-password
DB_HOST=db
DB_PORT=5432

# React 設定
REACT_APP_API_URL=http://localhost:8000
```

### 資料庫遷移

```bash
# 建立遷移檔案
python manage.py makemigrations

# 執行遷移
python manage.py migrate
```

### 執行測試

```bash
# 後端測試
cd backend
python manage.py test

# 前端測試
cd frontend
npm test
```

### 程式碼格式化

```bash
# Python (使用 Black)
cd backend
black .

# JavaScript (使用 Prettier)
cd frontend
npm run format
```

## 🐳 部署

### Docker 部署

詳細的 Docker 部署說明請參考 [專案說明文件.md](./專案說明文件.md) 中的「階段五：Docker 容器化部署」章節。

### 生產環境部署

1. 設定 `DEBUG=False`
2. 使用強密碼的 `SECRET_KEY`
3. 設定正確的 `ALLOWED_HOSTS`
4. 使用 PostgreSQL 資料庫
5. 設定 HTTPS
6. 使用 Nginx 作為反向代理
7. 設定適當的資源限制

## 🤝 貢獻

歡迎提交 Issue 和 Pull Request！

### 貢獻流程

1. Fork 本專案
2. 建立功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

### 提交訊息規範

- `feat`: 新功能
- `fix`: 修復 bug
- `docs`: 文件更新
- `style`: 程式碼格式調整
- `refactor`: 程式碼重構
- `test`: 測試相關
- `chore`: 建置過程或輔助工具的變動

## 📚 詳細文件

完整的開發文件、實作過程、學習重點等，請參考 [專案說明文件.md](./專案說明文件.md)。

## 🐛 問題回報

如果發現 bug 或有功能建議，請在 [Issues](https://github.com/你的使用者名稱/task-management-system/issues) 中提出。

## 📄 授權

本專案採用 MIT 授權條款。詳見 [LICENSE](LICENSE) 檔案。

## 👨‍💻 作者

[您的名字]

- GitHub: [@你的使用者名稱](https://github.com/你的使用者名稱)
- Email: your.email@example.com

## 🙏 致謝

- [Django](https://www.djangoproject.com/) - 強大的 Python Web 框架
- [React](https://react.dev/) - 現代化的前端框架
- [Django REST Framework](https://www.django-rest-framework.org/) - 優秀的 API 開發工具
- 所有為這個專案做出貢獻的開發者

## 📊 專案統計

![GitHub stars](https://img.shields.io/github/stars/你的使用者名稱/task-management-system?style=social)
![GitHub forks](https://img.shields.io/github/forks/你的使用者名稱/task-management-system?style=social)
![GitHub issues](https://img.shields.io/github/issues/你的使用者名稱/task-management-system)
![GitHub pull requests](https://img.shields.io/github/issues-pr/你的使用者名稱/task-management-system)

---

⭐ 如果這個專案對你有幫助，請給個 Star！
