#AirBnB clone_console

In the consoleare commands for create, update, destroy, show and manage diferent
classes and attributes for the items in the app for users.

#Console
* create data model
* create, update, destroy, objects through a console / command interpreter
* store and persist objects to a JSON file
The first stage is to manipulate a storage system. This storage will give us an
abstraction between “My object” and “How they are stored and persisted”.
So from the command interpreter and from the front-end and RestAPI to be built
later, there is no need take care of how objects are stored.
This abstraction will also allow to change the type of storage easily without
updating all of the codebase.
The console will be a tool to validate this storage engine

# Command interpreter

Our command interpreter resembles a mini shell and allow us manage the objects
of the project:

* Create a new object
* Retrieve an object from a file
* Do operations on objects
* Update attributes of an object
* Destroy an object

# Objectives of project

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

# Content of Directory #
* Models Folder: Classes of the project. BaseModel is the parent Class.
The other classes (amenity, city, place, review, state, user)
inherit from BaseModel and specify others attributes for itselfs.
* Tests Folder : Unittests for the project
* AUTHORS: Information about the authors
* console.py: Eceutable file for the console
* file.json: JSON file with all information of instances
