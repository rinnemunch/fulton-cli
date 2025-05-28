import datetime
import json
import os

FILE_PATH = "services.json"


def load_services():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_services(services):
    with open(FILE_PATH, "w") as file:
        json.dump(services, file, indent=4)


def show_status(verbose=False):
    services = load_services()
    print("\n📊 Service Status:\n")
    for name, enabled in services.items():
        status = "ENABLED ✅" if enabled else "DISABLED ❌"
        print(f" - {name.capitalize():<12}: {status}")
        if verbose:
            print(f"   ↪ Service key: '{name}', current value: {enabled}")
    print()


def log_action(action, service_name):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{action}] {service_name} at {timestamp}\n"
    with open("log.txt", "a") as file:
        file.write(entry)


def enable_service(service_name, log=False):
    services = load_services()
    if service_name not in services:
        print(f"❌ '{service_name}' is not a recognized service.")
        return
    services[service_name] = True
    save_services(services)
    print(f"✅ '{service_name}' has been enabled.")
    if log:
        log_action("Enabled", service_name)


def disable_service(service_name, log=False):
    services = load_services()
    if service_name not in services:
        print(f"❌ '{service_name}' is not a recognized service.")
        return
    services[service_name] = False
    save_services(services)
    print(f"🛑 '{service_name}' has been disabled.")
    if log:
        log_action("Disabled", service_name)


def reset_services():
    default_state = {
        "updates": False,
        "backups": False,
        "monitoring": False
    }
    save_services(default_state)
    print("🔄 All services have been reset to default (DISABLED).")
