START = """🛡️ <b>Welcome to Server Manager Bot!</b>

You can use this bot to monitor and control your Linux server.
"""

ACCESS_DENIED = "🚫 <b>Access denied.</b> You are not allowed to use this bot."

SERVER_STATUS = """
<b>📊 Server Status</b>

[System]
├ 🧠 CPU:  {cpu}% {cpu_bar}
├ 🌡️ CPU Temp:  {temp}
├ 📈 RAM:  {ram}% {ram_bar}
├ 🔃 Swap:  {swap}% {swap_bar}
└ 💾 Disk:  {disk}% {disk_bar}

[Processes]
├ 🧠 Top CPU:  {top_cpu}
└ 🧬 Top RAM:  {top_ram}

[Network]
├ 🏠 Local IP:  {local_ip}
└ 🌐 Public IP:  {ip}

[Uptime]
├ 📡 Uptime:  {uptime}
└ 🕒 Time:  {time}
"""
