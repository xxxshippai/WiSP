# WiSP

Launch main for tasks 2-4


Keybinds:
- R - start stop rotation
- 1-4 - figure types

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

Saved files format:
"Indices""Vertices""Color"
Both indices and vertices are lists of vec3 elements, each of saved data looking like this:
""x1,y1,z1""x2,y2,z2"..."
The lists of elements are read by shlex
Color is a single vec3 element represented by floats
