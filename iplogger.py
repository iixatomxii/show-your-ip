import requests
import datetime
import time

def get_public_ip():
    """Get the current public IP address using an external service."""
    try:
        response = requests.get("https://api.ipify.org?format=text", timeout=10)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

def log_ip_every_hour(log_file="public_ip_history_log.txt"):
    """Continuously log the public IP address every hour."""
    print(f"Starting Public IP logger. Logging to {log_file} every 1 hour.\nPress Ctrl+C to stop.\n")
    while True:
        ip = get_public_ip()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} -> {ip}"
        

        with open(log_file, "a") as f:
            f.write(entry + "\n")
        

        print(entry)
        

        time.sleep(3600)

if __name__ == "__main__":
    try:
        log_ip_every_hour()
    except KeyboardInterrupt:
        print("\nStopped by user.")
    except Exception as e:
        print("Error:", e)

    input("\nPress Enter to exit...")
