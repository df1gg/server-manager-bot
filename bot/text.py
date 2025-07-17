START = """🛡️ <b>Welcome to Server Manager Bot!</b>

You can use this bot to monitor and control your Linux server.
"""

ACCESS_DENIED = "🚫 <b>Access denied.</b> You are not allowed to use this bot."

SERVER_STATUS = """
<b>📊 Server Status</b>  <code>[{hostname}]</code>

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
├ 🌐 Public IP:  {ip}
├ ⬇️ Download:   {download}
├ ⬆️ Upload:     {upload}
└ 📦 Packets:    {packets_in} in / {packets_out} out

[Uptime]
├ 📡 Uptime:  {uptime}
└ 🕒 Time:  {time}
"""

SERVICES_MANAGER_LIST = """
🛠️ <b>Service Management</b>

Here you can manage your connected services.
Select one from the list below or add a new one.

Each service allows you to configure specific parameters, enable/disable it,
or remove it at any time.
"""
