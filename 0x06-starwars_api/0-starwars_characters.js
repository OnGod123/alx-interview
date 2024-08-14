#!/usr/bin/node

/**
 * This script prints all character names of a Star Wars movie
 * in the same order as they appear in the "characters" list from the
 * Star Wars API. The Movie ID is passed as the first command-line argument.
 */

const request = require('request');

/**
 * Makes a request to the Star Wars API to retrieve the list of characters
 * for a given movie ID and prints each character's name in the correct order.
 *
 * @param {string} movieId - The ID of the Star Wars movie.
 */
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) {
    throw err;
  }

  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});

/**
 * Recursively prints each character's name in the order they appear in the
 * "characters" list. It fetches each character's details using the URL provided
 * in the list.
 *
 * @param {array} actors - Array of character URLs from the Star Wars API.
 * @param {number} x - Index of the current character in the array to be printed.
 */
const exactOrder = (actors, x) => {
  if (x === actors.length) {
    return;
  }

  request(actors[x], function (err, res, body) {
    if (err) {
      throw err;
    }

    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};

