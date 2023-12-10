#!/usr/bin/python3
"""entry point of the command line interpreter"""
import cmd
import shlex
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """definition"""
    prompt = "(hbnb) "
    __classes = {"BaseModel", "User", "State", "City",
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
        if line not in HBNBCommand.__classes:
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
        if strings[0] not in HBNBCommand.__classes:
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
        if strings[0] not in HBNBCommand.__classes:
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
        if strings[0] not in HBNBCommand.__classes:
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
        if strings[0] not in HBNBCommand.__classes:
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
        storage.save()

    def strip_line(self, str):
        """strip line"""
        newstr = str[str.find("(")+1:str.rfind(")")]
        newstr = shlex.shlex(newstr, posix=True)
        newstr.whitespace += ','
        newstr.whitespace_split = True
        return list(newstr)

    def strip_dict(self, str):
        """try to find a dict while stripping line"""
        newstr = str[str.find("(")+1:str.rfind(")")]
        try:
            newdict = newstr[newstr.find("{")+1:newstr.rfind("}")]
            return eval("{" + newdict + "}")
        except:
            return None

    def default(self, line):
        """defaults"""
        subargs = self.strip_line(line)
        strings = list(shlex.shlex(line, posix=True))
        if strings[0] not in HBNBCommand.__classes:
            print("*** Unknown syntax: {}".format(line))
            return
        if strings[2] == "all":
            self.do_all(strings[0])
        elif strings[2] == "count":
            count = 0
            for obj in storage.all().values():
                if strings[0] == type(obj).__name__:
                    count += 1
            print(count)
            return
        elif strings[2] == "show":
            key = strings[0] + " " + subargs[0]
            self.do_show(key)
        elif strings[2] == "destroy":
            key = strings[0] + " " + subargs[0]
            self.do_destroy(key)
        elif strings[2] == "update":
            newdict = self.dict_strip(line)
            if type(newdict) is dict:
                for key, val in newdict.items():
                    keyVal = strings[0] + " " + subargs[0]
                    self.do_update(keyVal + ' "{}" "{}"'.format(key, val))
            else:
                key = strings[0]
                for arg in subargs:
                    key = key + " " + '"{}"'.format(arg)
                self.do_update(key)
        else:
            print("*** Unknown syntax: {}".format(line))
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
