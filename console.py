#!/usr/bin/python3
"""entry point of the command line interpreter"""
import cmd


class AirbnbConsole(cmd.Cmd):
    prompt = "(Airbnb) "

if __name__ == '__main__':
    AirbnbConsole().cmdloop()
