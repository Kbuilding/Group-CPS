// Define Particle class
function Particle(x, y, coords) {
  this.x = x; // x-coordinate of particle
  this.y = y; // y-coordinate of particle
  this.coords = coords; // set of coordinates for particle's path

  this.history = []; // set of coordinates for particle and its trail
  
  var i0 = 0 // Iterator that increments every time particle moves to next coordinate
  var i1 = i1 // Variable that will store modulus of iterator, to allow for infinite looping
  
  this.update = function () {
    var i1 = i0 % this.coords.length
    // Changes x and y location
    this.x = this.coords[i1][0] * 0.7; // Scaling the size of the country shape
    this.y = this.coords[i1][1] * 0.7; // Scaling the size of the country shape
    i0 += 1


    // Stores a copy of particle's x and y location in history, which is used to display the particle trail
    var v = createVector(this.x, this.y);
    this.history.push(v);

    // If history exceeds a certain length, remove the oldest entry in history. This controls the length of the particle trail.
    if (this.history.length > round(this.coords.length/1.5)) { // Currently calculates number of particles based on number of coordinates for country
      this.history.splice(0, 1);
    }
  };

  // Define object method 'show' for particle i.e. how the particle is displayed (e.g. size, colour, transparency)
  this.show = function () {

    // For 
    for (var i = 0; i < this.history.length; i++) {
      var pos = this.history[i];
      noStroke() // No outline

      fill(250,50,150,i * 100/this.history.length)  // Set colour, alpha of particle - alpha set using calculation that tries to find even distribution of alpha across number of particles in 'history' trail
      ellipse(pos.x, pos.y, 3, 3); // Set shape, position, size of particle
    }

  };
}
