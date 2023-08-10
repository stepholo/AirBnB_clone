#!/usr/bin/env python3
"""
This is the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing upon recieving an empty line."""
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program
        """
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
