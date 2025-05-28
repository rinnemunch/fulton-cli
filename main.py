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
    status_parser.add_argument('--verbose', action='store_true', help='Show extra debug info')

    # enable command
    enable_parser = subparsers.add_parser('enable', help='Enable a mock service')
    enable_parser.add_argument('--service', type=str, required=True, help='Service name to enable')
    enable_parser.add_argument('--log', action='store_true', help='Log the action')

    # disable command
    disable_parser = subparsers.add_parser('disable', help='Disable a mock service')
    disable_parser.add_argument('--service', type=str, required=True, help='Service name to disable')
    disable_parser.add_argument('--log', action='store_true', help='Log the action')

    args = parser.parse_args()

    if args.command == 'status':
        core.show_status(verbose=args.verbose)
    elif args.command == 'enable':
        core.enable_service(args.service, log=args.log)
    elif args.command == 'disable':
        core.disable_service(args.service, log=args.log)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
