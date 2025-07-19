START = """🛡️ <b>Welcome to Server Manager Bot!</b>

You can use this bot to monitor and control your Linux server.
"""

ACCESS_DENIED = "🚫 <b>Access denied.</b> You are not allowed to use this bot."

SERVER_STATUS = """
<b>📊 Server Status</b>  <code>[{hostname}]</code>

[System]
├ 💻 OS:  {os}
├ ⚙️ Kernel:  {kernel}
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

SERVICE_INFO = """
<b>🧰 Service Info</b>  <code>[{name}]</code>

[Status]
├ 🔌 Running:  {is_running}
├ 🔁 Auto-start:  {is_enabled}
└ 📦 PID:  {pid}

[Stats]
├ 🧠 CPU Usage:  {cpu}%
├ 💾 Memory:  {mem}%
└ 🕒 Uptime:  {uptime}

[Path]
└ 📍 {path}
"""

SERVICE_STOP_NOTIFY = "🚨 Service <b>{display_name}</b> has stopped unexpectedly!"
