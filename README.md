# WiSP

Launch main for tasks 2-4


Keybinds:
- R - start stop rotation
- T - command input
- U - manual update
- W,A,S,D - camera movement
- Mouse - camera pitch/yaw

FIGURES SET TO BUTTONS HAVE PRESET DIMENSIONS AND POSITIONS

Main commands:
"figure" "origin position" "rotation" "dimensions" - main figure creation command

Subcommands:
- rotate moving "rotation vector" - continuous rotation  on set axis
- rotate static "add/origin" "rotation vector" "angle" - rotate by angle, either from original position, or additive to previous rotation
- move "move vector" - move figure by vector
- color "rgb vector" - change figure color
- figure "figure type" - change figure without changing dimesions
- camera "perspective 1/ortho 2" "NEAR" "FAR" - change projection type as well as near and far parameters  
- load "file" "origin position" - load figure from file
- save "file" - save figure to file

Saved files formatting:
Each file contains 3 different lists.
- 1st list is a list of vertices including coordinates of each vertice.
- 2nd list is a list of indices including vertices making up each indice.
- 3rd list contains RGB color value of saved figure.

Below is an example of how saved file should look:
vertice1 " vertice2 " vertice3 # indice1 " indice2 " indice3 # color
- \# is a symbol that splits string into main lists of vertices, indices and color.
- " is a symbol that splits each of the main lists into sublists of coordinates.

Sublists of vertices, indices and color are separated by spaces, so:
- eg. vertice1 = 1.0 1.0 1.0
- eg. indice1 = 1 2 3

Vertices and color are saved as float values, while indices are integers.



