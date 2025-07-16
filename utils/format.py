def format_bytes(size: int) -> str:
    power = 1024
    units = ["B", "KB", "MB", "GB", "TB"]
    for unit in units:
        if size < power:
            return f"{size:.1f} {unit}"
        size /= power
    return f"{size:.1f} PB"
