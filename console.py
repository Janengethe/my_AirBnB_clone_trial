#!/usr/bin/python3
"""
contains the entry point to the command interpreter
"""


import cmd
import sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    command line interpreter
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ Interprets Ctrl + D """
        print()
        return True

    def do_quit(self, line):
        """ Quit command to exit the program: Type quit"""
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.
        It ignores the last nonempty
        command entered and does nothing"""
        pass

    def do_create(self, line):
        """Creates a new BaseModel instance
        Args:
            None
        Prints id of the new BaseModel instance
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            base1 = BaseModel()
            base1.save()
            print(base1.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name
        and id. Example: $ show BaseModel 1234-1234-1234.
        """
        a_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif a_list[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(a_list) == 1:
            print("** instance id missing **")
            return
        else:
            ke_y = a_list[0] + "." + a_list[1]
            all_instances = storage.all()
            if ke_y not in all_instances.keys():
                print("** no instance found **")
            else:
                class_dict = all_instances[ke_y]
                for k, v in class_dict.items():
                    if k == "__class__":
                        instance_class = v
                    if k == "id":
                        instance_id = v
                    if k == "created_at":
                        instance_created_at = v
                    if k == "updated_at":
                        instance_created_at = v
                print("[{}] ({}) {}".format(instance_class, instance_id, class_dict))

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id. Example: (hbnb)  destroy BaseModel 1234-1234-1234.
        """
        a_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif a_list[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(a_list) == 1:
            print("** instance id missing **")
            return
        else:
            ke_y = a_list[0] + "." + a_list[1]
            all_instances = storage.all()
            if ke_y not in all_instances.keys():
                print("** no instance found **")
            else:
                del all_instances[ke_y]
                storage.save()

    def do_all(self, line):
        """
        Prints the string representation of all instances 
         Example: (hbnb) all BaseModel  
          or (hbnb) all
        """
        obj_list = []
        a_list = line.split(" ")
        if a_list[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        all_instances = storage.all()
        for k, v in all_instances.items():
            if k:
                class_dict = all_instances[k]
            if v:
                for i, j in v.items():
                    if i == "__class__":
                        instance_class = j
                    if i  == "id":
                        instance_id = j
                    if i == "created_at":
                        instance_created_at = j
                    if i == "updated_at":
                        instance_created_at = j
                a_str = ("[{}] ({}) {}".format(instance_class, instance_id, class_dict))
                obj_list.append(a_str)
                print(obj_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: (hbnb) update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com".
        """
        a_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif a_list[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(a_list) == 1:
            print("** instance id missing **")
            return
        elif len(a_list) == 2:
            print("** attribute name missing **")
        elif len(a_list) == 3:
            print("** value missing **")
        else:
          ke_y = a_list[0] + "." + a_list[1]
          all_instances = storage.all()
          if ke_y not in all_instances.keys():
              print("** no instance found **")
          else:
              value = all_instances[ke_y]
              value[a_list[2]] = a_list[3]
              print(value)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
