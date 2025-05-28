# pro_client/core.py

services = {
    "updates": False,
    "backups": False,
    "monitoring": False
}


def show_status():
    print("\n📊 Service Status:\n")
    for name, enabled in services.items():
        status = "ENABLED ✅" if enabled else "DISABLED ❌"
        print(f" - {name.capitalize():<12}: {status}")
    print()


def enable_service(service_name):
    if service_name not in services:
        print(f"❌ '{service_name}' is not a recognized service.")
        return
    services[service_name] = True
    print(f"✅ '{service_name}' has been enabled.")


def disable_service(service_name):
    if service_name not in services:
        print(f"❌ '{service_name}' is not a recognized service.")
        return
    services[service_name] = False
    print(f"🛑 '{service_name}' has been disabled.")
