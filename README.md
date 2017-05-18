# Project - Office Space Allocation  

In the Andela, there are offices and Living spaces. A staff has the option of being allocated an Office_space but no living space,
but a fellow can be be allocated both, livind_space and office.
This project will  computerize the room allocation system for one facilities called The Dojo.
This system will be used to automatically allocate spaces to people at random.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The requirements are in the file

```
requirements.txt
```

### Installing

Install python in your system

$ sudo apt install python
```
Clone the repo:
HTTPS
```
$ git clone https://github.com/kanyoro-mungai/Office-Space-Allocation
```
SSH
```
$ git clone git@github.com:kanyoro-mungai/Office-Space-Allocation

Change Directory into the project folder
```
$ cd Office-Space-Allocation
```

Create a virtual environment with Python 3.5
```
$ virtualenv --python=python3.5 'yourenvname'
```

Activate the virtual environment you have just created
```
$ source yourenvname/bin/activate
```

Install the application's dependencies from requirements.txt to the virtual environment
```
$ (yourenvname) pip install -r requirements.txt
```

Run the tool in interactive mode:
```
$ (yourenvname) python main_app.py -i
```

Usage:
```
    Dojo  create_room <room_type> <room_name>...
    Dojo  add_person <name> <p_type> <accomodation>
    Dojo  (- i| --interactive)
    Dojo  (-h| --help)
```
Options:
```
   -i, --interactive  :Interactive Mode
    -h, --help         :Show this screen and exit.
    create_room        :create a room of a certain type
    add_person         :add a person to the system
    <room_type>        :office or living
    <room_name>        :enter a desired room name
    <name>             :the name of the person
    <p_type>           :indicate whether the person is staff or fellow
    [<accommodation>]  : y or Y if the person wants accommodation, if not leave blank

```

**Contributions are highly welcomed and appreciated**


## Libraries
[Docopt](https://github.com/docopt/docopt) - Docopt helps you create most beautiful command-line interfaces

## Authors
* **Kanyoro Mungai**

