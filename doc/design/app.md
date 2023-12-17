### kernel = cad tools

takes care of sketching and geometry

### app 
takes care of main loop, user interaction, configuration


### units

the cad_kernel does not deal with units. the app deals with units
mm are base, everything should be converted if necessary using e.g. value * Unit.METER