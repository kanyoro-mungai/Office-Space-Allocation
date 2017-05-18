"""
This app uses docopt with the built in cmd module to create rooms and people and then assign people to diffrent rooms.
Usage:
    Dojo  create_room <room_type> <room_name>...
    Dojo  add_person <name> <p_type> <accomodation>
    Dojo  (- i| --interactive)
    Dojo  (-h| --help)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from app.dojo import Dojo

new_dojo = Dojo()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to Andela Dojo Space Allocator' \
        + ' (type help for a list of commands.)'
    prompt = 'Dojo>>>'
    file = None


    @docopt_cmd
    def do_create_room(self, args):
        """
        usage: create_room <room_type> <room_name>...
        """
        room_name = args['<room_name>']
        room_type = args['<room_type>']
        for room in room_name:
            new_dojo.create_room(room_type, room)

    @docopt_cmd
    def do_add_person(self, arg):
        """
        usage: add_person <name> <p_type> [<accomodation>]

        """
        if arg['<accomodation>'] and arg['<p_type>'] == "fellow":
            name = arg['<name>']
            p_type = arg['<p_type>']
            new_dojo.add_person(name, p_type, accomodation = 'y')
        else:
            name = arg['<name>']
            p_type = arg['<p_type>']
            new_dojo.add_person(name, p_type)



    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)