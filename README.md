<h1 align="center" id="title">🛡️ Telegram Server Manager Bot</h1>

<p align="center">
  <img src="https://socialify.git.ci/df1gg/server-manager-bot/image?custom_language=Python&language=1&logo=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F3%2F35%2FTux.svg%2F1727px-Tux.svg.png&name=1&owner=1&stargazers=1&theme=Light" alt="server-manager-bot" width="640" height="320" />
</p>

<p align="center">
  <b>Minimal, secure and extensible Telegram bot to monitor and control your Linux server — from anywhere.</b>
</p>

---

## 🧾 Description

**Telegram Server Manager Bot** is a lightweight self-hosted bot that lets you:
- Check server status (uptime, RAM, CPU, disk, IP)
- Manage systemd services
- View logs
- Upload/download files

Ideal for hobbyists, sysadmins, and minimal Linux lovers who don’t want to deal with full dashboards like Cockpit or Netdata.

---

## 🧐 Features (planned)

- uptime, CPU, RAM, disk, IP
- start/stop/restart systemd services
- tail logs from systemd or files
- File upload & download through Telegram
- Whitelisted access via Telegram ID
- Environment-based config via `.env`

---

## 🛠️ Installation

1. **Clone the repo**

```bash
git clone https://github.com/df1gg/server-manager-bot.git && cd server-manager-bot
```

2. **Create and activate virtualenv**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create `.env` file**

```env
BOT_TOKEN=your_telegram_bot_token
OWNER_ID=your_telegram_numeric_id
```

5. **Run the bot**

```bash
python main.py
```

---

## 🍰 Contribution

Contributions are welcome!  
To contribute:

1. Fork the repository  
2. Create a feature branch  
3. Commit your changes  
4. Open a pull request  

Please keep the code clean and follow the project style.

---

## 💻 Built with

- **Python 3.11+**
- [Aiogram 3.x](https://github.com/aiogram/aiogram) — Telegram Bot Framework (async)
- `asyncio`, `subprocess`, `os`, `psutil` — Core system tools
- `systemd` — Background service handling
- `.env` — Secure environment-based config

---

## 🛡️ License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and share.

---

## 👤 Author

Made by [df1gg](https://github.com/df1gg) with ❤️

---

## 📌 TODO

- [ ] Implement `status` button  
- [ ] Add `services` management  
- [ ] Tail log files 
- [ ] File transfer (upload & download)  
- [ ] Systemd service for auto-run  
- [ ] Security: 2FA or password command  
- [ ] Docker integration  
