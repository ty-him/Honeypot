#Libraries
import argparse
from ssh_honeypot import *
import paramiko  # Import paramiko for SSH key handling
from web_honeypot import run, run_web_honeypot

# Parse Arguments

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="SSH Honeypot")
    parser.add_argument('-a', '--address', type=str, required= True)
    parser.add_argument('-p', '--port', type=int, required=True)
    parser.add_argument('-u', '--username', type=str, required=True)
    parser.add_argument('-pw', '--password', type=str, required=True) 

    parser.add_argument('-s', '--ssh', action="store_true")
    parser.add_argument('-w', '--http', action="store_true")

    args = parser.parse_args()

    # Load the host key for SSH
    host_key = paramiko.RSAKey(filename='server.key')  # Ensure you have a valid RSA key file

    try:
        if args.ssh:
            print("[-] Running SSH Honeypot...")
            honeypot(args.address, args.port, args.username, args.password)
            
            if not args.username:
                username = None
            if not args.password:
                password = None
        elif args.http:
            print("[-] Running HTTP Honeypot...")

            if not args.username:
                username = None
            if not args.password:
                password = None
            print(f"Port: {args.port}, Username: {args.username}, Password: {args.password}")
            run_web_honeypot(port=args.port, input_username=args.username, input_password=args.password)
            pass
        else:
            print("[-] Please specify a honeypot type: --ssh or --http")
    except:
        print("\n Extiing Honeypy...")

