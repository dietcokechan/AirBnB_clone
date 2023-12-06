#!/usr/bin/python3
"""entry point of the command line interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """exit program"""
        return True

    do_EOF = do_quit

    def emptyline(self):
        """do nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
