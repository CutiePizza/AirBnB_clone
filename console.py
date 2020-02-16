#!/usr/bin/python3
"""
Module that contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Command processor
    """

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """
        End-of-file marker
        """
        print("")
        return True

    def do_quit(self, line):
        """
        Quit the command line
        """
        return True

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.
        """
        pass

    def do_create(self, line):
        """
        Create an instance of BaseModel
        Usage: create <class Name>
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            my_class = BaseModel()
            my_class.save()
            print("{}".format(my_class.id))

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name
        and id.
        Usage: show <class Name> <id>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                key = args[0] + "." + args[1]
                obj = storage.all()
                if key in obj:
                    print(obj[key])
                else:
                    print("** no instance found **")


    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        Usage: Destroy <class Name> <id>
        """
        pass

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on
        the class name.
        Usage: all <class Name> or all
        """
        pass

    def do_update(self, class_name, class_id, attribute_name, attribute_value):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        pass


if __name__ == '__main__':
    import sys
    CtrlC = False
    while CtrlC != True:
        try:
            HBNBCommand().cmdloop()
            CtrlC = True
        except KeyboardInterrupt:
            sys.stdout.write('\n')
