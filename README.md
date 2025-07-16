> ⚠️ Project under active development — not stable yet.
Expect breaking changes and work-in-progress code

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

- Monitor server metrics (uptime, CPU, RAM, disk, swap, temperature, and more)
- Manage systemd services (start/stop/restart)
- View and tail logs from services or files
- Upload/download files directly through Telegram
- Inspect network: local/public IP, bandwidth usage, listening ports
- Identify top processes by CPU/RAM
- Whitelisted admin-only access

Ideal for hobbyists, sysadmins, and minimal Linux lovers who don’t want to deal with full dashboards like Cockpit or Netdata.

---

## 🧐 Features

- **System Metrics**: uptime, CPU, RAM, disk, swap, CPU temperature, load average
- **Network Info**: local/public IP, downloaded/uploaded bytes (human-readable), packet counts
- **Processes**: top CPU and RAM consumers
- **Hostname**: server identifier in status header
- **Security**: access limited by Telegram ID(s) & access logs
- **Extensible**: modular utilities, middleware, and decorators for easy expansion

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
OWNER_IDS=123456789,987654321   # comma-separated list of admin IDs or one ID
```

5. **Run the bot**

```bash
python main.py
```

---

## 🍰 Contribution

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "feat: your feature description"`)
4. Push and open a Pull Request against `dev`

Please keep the code clean and follow the project style.

---

## 💻 Built with

- **Python 3.11+**
- [Aiogram 3.x](https://github.com/aiogram/aiogram) — Telegram Bot Framework (async)
- `asyncio`, `socket`, `os`, `psutil` — Core system tools
- `loguru` — structured and colorized logging
- `systemd` — Background service handling
- `dotenv` — Secure environment-based config

---

## 🔐 Security & Access Control

- Only IDs in `OWNER_IDS` can interact with the bot
- Unauthorized users receive a `⛔ Access denied` message and no handlers run
- Flexible middleware and decorator support for further restrictions or authentication

---

## 📌 TODO

### 🟢 MVP / Must-have

- [x] Display server status info with inline refresh button
- [x] Admin-only access control by Telegram ID(s)
- [ ] Service management
  - Automatic discovery of available systemd services
  - Add/remove services from management list
- [ ] OS version display (distribution and kernel)
- [ ] Auto-refresh status periodically
- [ ] Reboot & Poweroff functionality

### 🔵 Nice-to-have (v1)

- [ ] Docker integration: list containers, start/stop/restart via buttons
- [ ] Graphs: CPU/RAM/Disk/Swap usage over the last hours
- [ ] Alerts & Notifications: send Telegram alerts on high load or service failure
- [ ] Port scanner: list listening TCP ports with process names
- [ ] Cron-manager: add/remove cron jobs via bot commands
- [ ] Log search: grep-like filtering of logs

### ⚫️ Future / Extras

- [ ] Internationalization (i18n) — multi-language support
- [ ] CI/CD trigger — deploy or tests via bot
- [ ] Batch commands execution — run multiple commands in sequence

---

## 🛡️ License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and share.

---

## 👤 Author

Made by [df1gg](https://github.com/df1gg) with ❤️
