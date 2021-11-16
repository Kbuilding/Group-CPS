//This project was completed for CECS8001 (Build course) Semester 2 as part of the Master of Applied Cybernetics at the ANU School of Cybernetics.

//References:
//https://www.youtube.com/watch?v=vqE8DMfOajk
//https://editor.p5js.org/Kumu-Paul/sketches/wq3Uh5dBp

// Go to code above and check lines 70-88 to see how different types of coordinate nodes are treated

// Initialise variable that will store particle object
var particle;
var converted_global_coords = []
var global_particles = []
var converted_particles = []



// DEFAULT p5.js FUNCTION - this is where we define the particles we want to display on the map
function setup() {
  createCanvas(4000,4000);
  // Convert coordinates in country.js to coordinates that can be used for visualisation
  for (let i = 0,i_converted = 0; i < global_coords.length; i++) {
    // Skip country if it has a heartrate of '0' in country.js
    if(global_coords[i][0] > 0) {
      converted_global_coords[i_converted] = new Coord_Conversion(global_coords[i])
      i_converted ++ // Only increment i_converted if a new set of coordinates is added (i.e. if the country heartrate is greater than 0)
    } else {
      continue // If country average heartrate is less than or equal to 0, then skip (i.e. don't add it)
    }
    
  }

  // Initialise particles to visualise each country
  for (let i_2 = 0; i_2 < converted_global_coords.length; i_2++) {
    global_particles[i_2] = new Particle(converted_global_coords[i_2][0][0],converted_global_coords[i_2][0][1],converted_global_coords[i_2])
  }
  
}



// DEFAULT p5.js FUNCTION - this is where we tell the program to display the particles
function draw() {
  background(0);
  
// Display the particles
  // global_particles[0].update()
  // global_particles[0].show()
  
  // 
  for (let i_3 = 0; i_3 < global_particles.length; i_3++) {
    global_particles[i_3].update()
    global_particles[i_3].show()
  }

}


//-------------------
