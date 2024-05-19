# AirBnB Clone - The Console
<div style="text-align: center;">
  <img src="/root/alx/AirBnB_clone/hbnb.png" alt="Hbnb" width="800"/>
</div>

---

<div style="text-align: center;">
  <img src="/root/alx/AirBnB_clone/console.png" alt="AirBnB Clone" width="800"/>
</div>

## Description of the Project

This project is an initiative to create a simplified version of the AirBnB application, focusing on the backend console interface. It involves developing a command-line interpreter to manage the application's data models and storage. This console allows users to create, read, update, and delete objects, simulating the basic functionalities needed for managing an AirBnB-like platform.

The project is structured to follow a series of tasks aimed at gradually building a robust backend system. Key components include:
- Custom command interpreter.
- Class definitions for various object types (e.g., User, Place, City, Amenity, Review).
- Persistent storage using file serialization.

### Files and Directories

- `models` : contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- `tests` : contain all unit tests.
- `console.py` : file is the entry point of our command interpreter.
- `models/base_model.py` : file is the base class of all our models. It contains common elements:
    - `attributes` : id, created_at and updated_at
    - `methods` : save() and to_json()
- `models/engine` : directory will contain all storage classes (using the same prototype). For the moment I will have only one: file_storage.py.
---
## Description of the Command Interpreter

> The command interpreter is the central feature of this project. It functions as a REPL (Read-Eval-Print Loop), enabling users to interact with the backend system through text-based commands.


### How to Start the Command Interpreter
- Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
```
- But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Testing
Unittests for the project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:
```
$ python3 unittest -m discover tests
```
Alternatively, you can specify a single test file to run at a time:
```
$ python3 unittest -m tests/test_console.py
```
