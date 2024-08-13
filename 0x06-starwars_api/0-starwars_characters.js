#!/usr/bin/env node

// Import the 'request' module to handle HTTP requests
const request = require('request');

/**
 * Fetches and prints the names of characters from a Star Wars movie.
 * 
 * This script takes a Movie ID as the first command-line argument, retrieves
 * the movie's details from the Star Wars API, and then prints the names of
 * all characters featured in that movie.
 * 
 * Usage:
 * node script.js <MovieID>
 * 
 * Example:
 * node script.js 3
 * 
 * The above command will fetch and print the names of characters from "Return of the Jedi".
 */

// Fetch the movie details using the provided Movie ID
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err; // Throw an error if the request fails

  // Parse the response body as JSON and extract the list of character URLs
  const actors = JSON.parse(body).characters;

  // Start processing the character URLs in the exact order
  exactOrder(actors, 0);
});

/**
 * Processes each character URL one by one and prints the character's name.
 * 
 * @param {Array} actors - Array of character URLs
 * @param {number} x - Current index in the actors array
 */
const exactOrder = (actors, x) => {
  if (x === actors.length) return; // Exit when all characters are processed

  // Fetch details of the character from the provided URL
  request(actors[x], function (err, res, body) {
    if (err) throw err; // Throw an error if the request fails

    // Parse the response body as JSON and print the character's name
    console.log(JSON.parse(body).name);

    // Recursively process the next character URL
    exactOrder(actors, x + 1);
  });
};

