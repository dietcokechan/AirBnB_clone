#!/usr/bin/python3
"""entry point of the command line interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {"BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"}

    def do_quit(self, line):
        """exit program"""
        return True

    do_EOF = do_quit

    def emptyline(self):
        """do nothing"""
        pass

    def do_create(self, line):
        """creates an object"""
        if not len(line):
            print("** class name missing **")
            return
        if line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        obj = eval(line)()
        print(obj.id)
        obj.save()

    def do_show(self, line):
        """shows an object"""
        if not len(line):
            print("** class name missing **")
            return
        strings = split(line)
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
            return
        keyVal = strings[0] + '.' + strings[1]
        if keyVal not in storage.all().keys():
            print("** no instance found **")
        else:
            print(storage.all()[keyVal])

    def do_destroy(self, line):
        """destroys an object"""
        if not len(line):
            print("** class name missing **")
            return
        strings = split(line)
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
            return
        keyVal = strings[0] + '.' + strings[1]
        if keyVal not in storage.all().keys():
            print("** no instance found **")
            return
        del storage.all()[keyVal]
        storage.save()

    def do_all(self, line):
        """print all"""
        if not len(line):
            print([obj for obj in storage.all().values()])
            return
        strings = split(line)
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        print([obj for obj in storage.all().values()
               if strings[0] == type(obj).__name__])

    def do_update(self, line):
        """updates an object"""
        if not len(line):
            print([obj for obj in storage.all().values()])
            return
        strings = split(line)
        for str in strings:
            if str.startswith('"') and str.endswith('"'):
                str = str[1:-1]
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing")
            return
        keyVal = strings[0] + '.' + strings[1]
        if keyVal not in storage.all().key():
            print("** no instance found **")
            return
        if len(strings) == 2:
            print("** attribute name missing **")
            return
        if len(strings) == 3:
            print("** value missing **")
            return
        try:
            setattr(storage.all()[keyVal], strings[2], eval(strings[3]))
        except Exception:
            setattr(storage.all()[keyVal], strings[2], strings[3])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
