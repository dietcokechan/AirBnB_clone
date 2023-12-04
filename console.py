#!/usr/bin/python3
"""entry point of the command line interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def quitcmd(self, line):
        """exit program"""
        return True
    
    cmdEOF = quitcmd

    def emptyline(self):
        """do nothing"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
