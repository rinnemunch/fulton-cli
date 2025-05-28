# FultonCLI

A Python-based command-line tool for managing mock system services.

This CLI tool simulates service enable/disable workflows in a Linux-style environment, using `argparse`, persistent JSON storage, and optional logging.

---

## 🔧 Features

- `status` — View current service states
- `enable` / `disable` — Toggle services by name
- `--log` — Log all actions to `log.txt`
- `--verbose` — Show internal debug info
- `reset` — Reset all services to default disabled state

---

## 💻 Usage

```bash
# Check current service status
python main.py status

# Enable a service and log it
python main.py enable --service updates --log

# Disable a service without logging
python main.py disable --service backups

# Show extra details with --verbose
python main.py status --verbose

# Reset all services to default (disabled)
python main.py reset
```

📂 Project Structure
FultonCLI/
├── main.py
├── pro_client/
│   └── core.py
├── services.json
├── log.txt
└── README.md

## 📈 Why This Project Exists
This project was created as a hands-on way to demonstrate real-world Python development concepts including: 
- Command-line interface design with argparse
- Modular code organization
- Persistent state using json
- File-based action logging
- CLI flag handling (--log, --verbose) 
Originally inspired by the kind of tooling used in Linux environments like Canonical's Ubuntu Pro Client, FultonCLI was built to be expanded or adapted based on the needs of future developer roles.