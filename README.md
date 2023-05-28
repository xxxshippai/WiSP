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
load "file" "origin position" - load figure from file
save "file" - save figure to file

Subcommands:
- rotate moving "rotation vector" - continuous rotation  on set axis
- rotate static "add/origin" "rotation vector" "angle" - rotate by angle, either from original position, or additive to previous rotation
- move "move vector" - move figure by vector
- color "rgb vector" - change figure color
- figure "figure type" - change figure without changing dimesions
- camera "perspective 1/ortho 2" "NEAR" "FAR" - change projection type as well as near and far parameters  

Saved files formatting:\n
Each file contains 3 different lists.\n
1st list is a list of vertices including coordinates of each vertice.\n
2nd list is a list of indices including vertices making up each indice.\n
3rd list contains RGB color value of saved figure.\n

Below is an example of how saved file should look:\n
vertice1 " vertice2 " vertice3 # indice1 " indice2 " indice3 # color\n
\# is a symbol that splits string into main lists of vertices, indices and color.\n
" is a symbol that splits each of the main lists into sublists of coordinates.\n

Sublists of vertices, indices and color are separated by spaces, so:\n
eg. vertice1 = 1.0 1.0 1.0\n
eg. indice1 = 1 2 3\n

Vertices and color are saved as float values, while indices are integers.\n
