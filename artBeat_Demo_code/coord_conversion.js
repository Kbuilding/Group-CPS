// Converts relative coordinates (i.e. point B is given as a relative position from point A) to global coordinates (i.e. point B is defined independently of point A from a global coordinate system)

function Coord_Conversion(relative_coords) {
  // Initialise variables for coordinate conversion (from relative to global)
  this.coords = relative_coords;
  // print("this.coords is: ", this.coords);
  this.converted_coord = [];
  this.converted_global_coords = [];

  
  
  // Hard-coded starting point for coordinates (adjust based on "m" and "z" tags in reference code)
  this.converted_coord_x = 0;
  this.converted_coord_y = 0;

    
    
  // Convert relative coordinates to global coordinates
  for (var c = 1; c < this.coords.length; c++) {
    var repeats = 0; // Iterator

    this.converted_coord_x += this.coords[c][0]*1.5; //Can be multiplied to scale x-coord
    this.converted_coord_y += this.coords[c][1]*1.5; //Can be multipled to scale y-coord

    while (repeats < this.coords[0]) { // Heartrate for each country is given as the first value for each country coords array in country.js
      // Setting speed (hard-coded hack-y method) by essentially repeating each coordinate for the number of times specified (e.g. repeats < 1000 means each coordinate is repeated 1000 times so the particle has to move slower as it is spending 1000x as long at each coordinate)
      this.converted_coord = [this.converted_coord_x, this.converted_coord_y];
      this.converted_global_coords.push(this.converted_coord);
      repeats++;
    }
  }
  return this.converted_global_coords;
}
