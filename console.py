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
# show: Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
# If the class name is missing, print ** class name missing ** (ex: $ show)
# If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
# If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
# If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)
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
    
    # # def do_show(self, arg):
    # """Prints the string representation of an instance based on the class name and id."""
    # args = arg.split()
    # if len(args) == 0:
    #     print("** class name missing **")
    # elif len(args) == 1:
    #     print("** instance id missing **")
    # elif args[0] not in self.__classes:
    #     print("** class doesn't exist **")
    # else:
    #     dic = models.storage.all()
    #     key = args[0] + '.' + str(args[1])
    #     if key in dic:
    #         print(dic[key])
    #     else:
    #         print("** no instance found **")
    # return



    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
