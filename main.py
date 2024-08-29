#!/usr/bin/env python3
import subprocess
import argparse

def run_command(command):
    print(command + " was printed!")

def main():
    parser = argparse.ArgumentParser(description="Run terminal commands from Python.")
    parser.add_argument('command', nargs='+', help="The command you want to run")
    args = parser.parse_args()
    command = ' '.join(args.command)
    run_command(command)

if __name__ == "__main__": main()