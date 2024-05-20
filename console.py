#!/usr/bin/python3
"""Define our command class"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Define HBNBCommand class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """End of life of the console"""
        return True
    
    def emptyline(self):
        """Do nothing when enter empty line"""
        pass
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
