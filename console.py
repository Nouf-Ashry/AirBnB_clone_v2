#!/usr/bin/python3
""" class the HBnB"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def editor(arg):
    bracurl = re.search(r"\{(.*?)\}", arg)
    brasqu = re.search(r"\[(.*?)\]", arg)
    if bracurl is None:
        if brasqu is None:
            return [i.strip(",") for i in split(arg)]
        else:
            z = split(arg[:brasqu.span()[0]])
            u = [i.strip(",") for i in z]
            u.append(brasqu.group())
            return u
    else:
        z = split(arg[:bracurl.span()[0]])
        u = [i.strip(",") for i in z]
        u.append(bracurl.group())
        return u


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand

    Attributes:
        prompt (str): The command prompt.
    """

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

    def emptyline(self):
        """pass empty line."""
        pass

    def default(self, arg):
        """radix  for cmd module when input is invalid"""
        forall = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        ch = re.search(r"\.", arg)
        if ch is not None:
            input1 = [arg[:ch.span()[0]], arg[ch.span()[1]:]]
            ch = re.search(r"\((.*?)\)", input1[1])
            if ch is not None:
                comnd = [input1[1][:ch.span()[0]], ch.group()[1:-1]]
                if comnd[0] in forall.keys():
                    hl = "{} {}".format(input1[0], comnd[1])
                    return forall[comnd[0]](hl)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """exit the program."""
        return True

    def do_EOF(self, arg):
        """exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id
        """
        try:
            if not args:
                raise SyntaxError()
            arg_list = args.split(" ")
            kw = {}
            for arg in arg_list[1:]:
                arg_splited = arg.split("=")
                arg_splited[1] = eval(arg_splited[1])
                if type(arg_splited[1]) is str:
                    arg_splited[1] = arg_splited[1].replace("_", " ").replace('"', '\\"')
                kw[arg_splited[0]] = arg_splited[1]
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        new_instance = HBNBCommand.classes[arg_list[0]](**kw)
        new_instance.save()
        print(new_instance.id)

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id
        """
        in1 = editor(arg)
        dobj = storage.all()
        if len(in1) == 0:
            print("** class name missing **")
        elif in1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(in1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(in1[0], in1[1]) not in dobj:
            print("** no instance found **")
        else:
            print(dobj["{}.{}".format(in1[0], in1[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and
        id (save the change into the JSON file)
        """
        in1 = editor(arg)
        dobj = storage.all()
        if len(in1) == 0:
            print("** class name missing **")
        elif in1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(in1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(in1[0], in1[1]) not in dobj.keys():
            print("** no instance found **")
        else:
            del dobj["{}.{}".format(in1[0], in1[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name
        """
        in1 = editor(arg)
        if len(in1) > 0 and in1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            inobj = []
            for inobject in storage.all().values():
                if len(in1) > 0 and in1[0] == inobject.__class__.__name__:
                    inobj.append(inobject.__str__())
                elif len(in1) == 0:
                    inobj.append(inobject.__str__())
            print(inobj)

    def do_count(self, arg):
        """the number of instances of a given class"""
        in1 = editor(arg)
        c = 0
        for obj in storage.all().values():
            if in1[0] == obj.__class__.__name__:
                c += 1
        print(c)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by
        adding or updating attribute"""
        in1 = editor(arg)
        dobj = storage.all()

        if len(in1) == 0:
            print("** class name missing **")
            return False
        if in1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(in1) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(in1[0], in1[1]) not in dobj.keys():
            print("** no instance found **")
            return False
        if len(in1) == 2:
            print("** attribute name missing **")
            return False
        if len(in1) == 3:
            try:
                type(eval(in1[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(in1) == 4:
            inobject = dobj["{}.{}".format(in1[0], in1[1])]
            if in1[2] in inobject.__class__.__dict__.keys():
                typ = type(inobject.__class__.__dict__[in1[2]])
                inobject.__dict__[in1[2]] = typ(in1[3])
            else:
                inobject.__dict__[in1[2]] = in1[3]
        elif type(eval(in1[2])) == dict:
            ino = dobj["{}.{}".format(in1[0], in1[1])]
            for i, j in eval(in1[2]).items():
                if (i in ino.__class__.__dict__.keys() and
                        type(ino.__class__.__dict__[i]) in {str, int, float}):
                    typ = type(ino.__class__.__dict__[i])
                    ino.__dict__[i] = typ(j)
                else:
                    ino.__dict__[i] = j
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
