# Contributing to Server Manager Bot

Thanks for your interest in contributing! ❤️  
Here are some guidelines to help you get started.

---

## 📋 Before You Begin

- Please read our [Code of Conduct](./CODE_OF_CONDUCT.md)
- Make sure there's no similar open issue or pull request
- For questions, feel free to open a discussion or issue

---

## 🛠️ Setting Up Your Environment

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

4. **Create ``.env`` file**

```env
BOT_TOKEN=your_telegram_bot_token
OWNER_IDS=123456789,987654321   # comma-separated list of admin IDs or one ID
```

5. **(Recommend) Allow the bot to use systemctl without sudo password**

If you want the bot to manage system services (start, stop, restart) via ``systemctl``, your user must be allowed to use it without entering a password.

- First, find the full path to systemctl:
```bash
which systemctl
```
(Usually it's ``/bin/systemctl``)

- Then open sudoers file:
```bash
# Option 1 — nano (easy for beginners)
sudo EDITOR=nano visudo

# Option 2 — vim
sudo EDITOR=vim visudo
```

- Add this line at the bottom, replacing ``yourusername`` with your actual username:
```bash
yourusername ALL=(ALL) NOPASSWD: /bin/systemctl
```
(Replace ``/bin/systemctl`` with actual path if different)

⚠️ Be careful: always use ``visudo`` to avoid syntax errors!

6. **Run the bot**

```bash
python main.py
```

## 🚀 How to Contribute

### 🐛 Reporting Bugs
- Describe the issue clearly
- Add logs or screenshots if possible
- Use the issue template if provided

### 🌟 Feature Requests
- Explain what and why
- Check if similar idea already exists

### 💡 Making Changes
1. Fork the repository
2. Create a new branch:
```sh
git checkout -b feat/your-feature-name
```
3. Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
4. Make sure your code is clean and documented

### 📦 Submitting a Pull Request
- PR title must follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- Link to related issues in description
- Be clear, polite, and descriptive 🙌
