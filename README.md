# Patl 

Patl is a Python package which helps you in creating a monitorable structure 
for your files and folder for your next big project.

## Installing
--------------

Install and update using `pip`:

```cmd

    > pip install patl

```


## A Simple Example
---------------------

In order to use patl you first have to create a patl.json file in your project's root area.

Inside patl.json you have to structure your files and folder in such a perfect manner that 
how you wanted to arrange them and afterall we are all doing this is a JSON file we have to
follow a certain kind of rules in order to structure our project.

- Each file and folder's name must be as key holder.

- Each file's value must be null to recognize it as a file.

```json
e.g: 
    { "index.js" : null }

```

- Each folder's value must be {} to recognize it as a folder.

``` json
e.g:
    { 
        "empty_folder" : {},
        "folder":{ "index.js" : null } 
    }
    
```

After constructing your structure in patl.json file you have to open your terminal and 
change your current working directory to folder where patl.json file is located.

### To Create Project Layout
-----------------------------

Here you have to use `-c` flag in order to create files and folders as you described inside patl.json
```cmd
    path/to/patl.json> patl -c
```

### To Remove Project Layout
-----------------------------

Here you have to use `-r` flag in order to remove files and folders as you described inside patl.json
```cmd
    path/to/patl.json> patl -r
```


Links
-----

-   Releases: https://test.pypi.org/project/Patl/
-   Code: https://github.com/Ajay1290/patl
-   Issue tracker: https://github.com/Ajay1290/patl/issues