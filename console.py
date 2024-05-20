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
        """Prints the string representation"""
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

    def do_all(self, arg):
        """Prints all string representation of class name."""
        args = arg.split()
        if len(args) > 0 and args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            all_objs = models.storage.all()
            if len(args) > 0:
                # Filter objects by the class name provided.
                filtered_objs = [str(obj) for key, obj in all_objs.items() if args[0] in key]
                print(filtered_objs)
            else:
                # Print all objects if no class name is provided.
                print([str(obj) for obj in all_objs.values()])

    def do_update(self, arg):
        """Updates an instance."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        key = args[0] + "." + args[1]
        dic = models.storage.all()
        if key not in dic:
            print("** no instance found **")
            return

        instance = dic[key]
        attribute_name = args[2]
        attribute_value = args[3].strip("\"")

        if attribute_name in ['id', 'created_at', 'updated_at']:
            print(f"** {attribute_name} can't be updated **")
            return

        try:
            typedata = type(getattr(instance, attribute_name))
            attribute_value = typedata(attribute_value)
        except (ValueError, TypeError):
            print("** invalid attribute value **")
            return

        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
