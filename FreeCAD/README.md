The FreeCAD portion of this project is a little weird as it relies on the
built in functionality to add macros as buttons within FreeCAD. A tutorial on
how to do this can be found here: https://wiki.freecadweb.org/Customize_Toolbars.\
 FreeCAD itself can be downloaded here: https://www.freecadweb.org/downloads.php

The PNG file used for the button has also been included so that the appearance
of FreeCAD can be emulated.

The macro itself is a python script with a unique file extension if you add the
following lines (assuming you use VS Code) to your settings.json file then it
will activate syntax highlighting.
```
    "files.associations": {
        "*.FCMacro": "python"
    }, 
```
This will make reading the file much easier. There are a lot of paths that
relate specifically to my primary device, as it was going to be used for testing
and the project was not about making a polished piece of software but rather
making something that could be used in the user study. As far as I am aware I
have marked these with comments.