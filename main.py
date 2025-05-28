import argparse
from pro_client import core


def main():
    parser = argparse.ArgumentParser(
        prog='FultonCLI',
        description='Mock service manager tool for Linux systems.'
    )

    subparsers = parser.add_subparsers(dest='command')

    # status command
    status_parser = subparsers.add_parser('status', help='Check current service status')

    # enable command
    enable_parser = subparsers.add_parser('enable', help='Enable a mock service')
    enable_parser.add_argument('--service', type=str, required=True, help='Service name to enable')

    # disable command
    disable_parser = subparsers.add_parser('disable', help='Disable a mock service')
    disable_parser.add_argument('--service', type=str, required=True, help='Service name to disable')

    args = parser.parse_args()

    if args.command == 'status':
        core.show_status()
    elif args.command == 'enable':
        core.enable_service(args.service)
    elif args.command == 'disable':
        core.disable_service(args.service)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
