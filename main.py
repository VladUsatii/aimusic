#!/usr/bin/env python3
import subprocess
import argparse

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout.decode('utf-8'))
    if result.stderr:
        print(result.stderr.decode('utf-8'))

def main():
    parser = argparse.ArgumentParser(description="Run terminal commands from Python.")
    parser.add_argument('command', nargs='+', help="The command you want to run")
    args = parser.parse_args()
    command = ' '.join(args.command)
    run_command(command)

if __name__ == "__main__": main()