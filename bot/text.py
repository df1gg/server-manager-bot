START = """🛡️ <b>Welcome to Server Manager Bot!</b>

You can use this bot to monitor and control your Linux server.
"""

ACCESS_DENIED = "🚫 <b>Access denied.</b> You are not allowed to use this bot."

SERVER_STATUS = """
<b>📊 Server Status</b>

[System]
├ 🧠 CPU:   {cpu}%  {cpu_bar}
├ 📈 RAM:   {ram}%  {ram_bar}
└ 💾 Disk:  {disk}% {disk_bar}

[Network]
├ 🏠 Local IP:  {local_ip}
└ 🌐 Public IP: {ip}

[Uptime]
├ 📡 Uptime:    {uptime}
└ 🕒 Time:      {time}
"""
