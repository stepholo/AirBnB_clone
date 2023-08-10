#!/usr/bin/env python3
"""
This is the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on
        the classname and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = args[0] + "." + args[1]
            all_objs = storage.all()
            if obj_id in all_objs:
                print(all_objs[obj_id])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into a JSON file)
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = args[0] + "." + args[1]
            all_objs = storage.all()
            if obj_id in all_objs:
                del all_objs[obj_id]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Usage: all or all <class name>
        """
        all_objs = storage.all()
        args = arg.split()
        if not args:
            print([str(obj) for obj in all_objs.values()])
        elif args[0] in ["BaseModel"]:
            print([str(obj) for key, obj in all_objs.items()
                   if args[0] in key])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the classname and id by adding or updating
        attribute (save the change into the JSON file).
        Usage: update <classname> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = args[0] + "." + args[1]
            all_objs = storage.all()
            if obj_id in all_objs:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    key = args[2]
                    if key in ["id", "create_at", "updated_at"]:
                        return
                    setattr(all_objs[obj_id], key, args[3].replace('"', ''))
                    all_objs[obj_id].save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
