### kernel = cad tools

takes care of sketching and geometry

### app 
takes care of main loop, user interaction, configuration

### units

the cad_kernel does not deal with units. the app deals with units
mm are base, everything should be converted if necessary using e.g. value * Unit.METER

## separation of user stuff and cad kernel

- The CAD kernel should in general be raising errors, while the app will handle them if they are 
relevant to the user. e.g. I run update on the sektch. it errors. The error should be returned, and the app should decide whether to retry or not. 

- Pop up warnings to the user should be issued by the app upon receiving the error, and if the decision is to retry, that is just issuing again the command to the kernel.

- Kernel app split also solves for example: sketch objects direct edits == where sketch objects should be edited through the sketch so that it can update it's state. from the app, geometry objects should not be accessible or directly editable.

- kernel does not implement user-facilitating methods e.g. sketch object does not have an edit() method that takes the user to the sketch. The app would have this, and it would follow the reference to the sketch.

### Undo stack

Another separation between app and kernel. The app maintains undo functionality. The kernel has no knowledge of the concept of undo, it jsut has state and ways to edit the state.
e.g. translate. The app tracks a translate command. The undo method, simply repeats a translate on the kernel but with negative of the initial values. This means, the kernel methods should be possible to be done in reverse. 
e.g. addition of object: app calls the addObject method, the undo would call the delete object method of the kernel


## Documents

app tracks documents that are related. should documents have dpendencies? part -> sketch ?