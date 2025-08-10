# MCP Resume Scorer with Leaderboard

Welcome to the MCPs repository! This project showcases custom MCP server implementations designed to provide AI models with secure, contextual access to tools and data. Whether you're building resume scoring endpoints, integrating OAuth, or experimenting with FastAPI and Gemini, this repo is your playground for creative, real-world AI utilities.

---

## 🚀 Features

- ✅ Resume scoring with AI-based feedback  
- 🔐 Google OAuth integration for secure access  
- ⚡ FastAPI endpoints with robust error handling  
- 🧪 Swagger UI for easy testing and documentation  
- 🌐 ngrok tunneling for public access and webhook testing  

---

## 📁 Project Structure

```
mcp-starter-main/
├── mcp-bearer-token/
│   ├── app.py                # Flask app with OAuth and token handling
│   ├── credentials.json      # Google OAuth secrets (not committed)
│   ├── requirements.txt      # Python dependencies
│   └── README.md             # You're reading it!
```

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Mokksh-bhatt/MCPs.git
cd MCPs/mcp-bearer-token
```

### 2. Create a virtual environment

```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Google OAuth credentials

- Download `credentials.json` from [Google Cloud Console](https://console.cloud.google.com/)
- Place it in the project root
- If named differently, set the environment variable:

```powershell
$env:GOOGLE_CLIENT_SECRETS = "your_file_name.json"
```

### 5. Run the server

```bash
python app.py
```

---

## 🌍 Expose Locally with ngrok

```bash
ngrok http 5000
```

Visit `http://127.0.0.1:4040` for the ngrok dashboard and copy your public URL.

---

## 🧠 Future Plans

- Add leaderboard scoring and resume feedback visualization  
- Integrate Gemini fallback models  
- Deploy to cloud platforms for persistent access  

---

## 🤝 Contributing

Pull requests, ideas, and feedback are welcome! Feel free to fork and build your own MCP extensions.

---

## 📄 License

This project is open-source under the MIT License.

---

## ✨ Author

Built with curiosity and creativity by [Mokksh Bhatt](https://github.com/Mokksh-bhatt)
