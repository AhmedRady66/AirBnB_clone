#!/usr/bin/python3
"""Define our command class"""

import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """Define HBNBCommand class"""
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """End of life of the console"""
        return True
    
    def emptyline(self):
        """Do nothing when enter empty line"""
        pass

    def do_create(self, arg):
        """Create new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        elif arg in self.__classes:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            dic = models.storage.all()
            key = arg[0] + '.' + str(arg[1])
            if key in dic:
                print(dic[key])
            else:
                print("** no instance found **")
        return

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            dic = models.storage.all()
            key = arg[0] + '.' + str(arg[1])
            if key in dic:
                del(dic[key])
            else:
                print("** no instance found **")
        return


    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
