#!/usr/bin/node

const request = require('request');

function printMovieCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const filmData = JSON.parse(body);
      const characters = filmData.characters;

      characters.forEach((characterUrl) => {
        request(characterUrl, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          } else {
            console.log(`Failed to fetch character data for ${characterUrl}`);
          }
        });
      });
    } else {
      console.log(`Failed to fetch movie data for movie ID ${movieId}`);
    }
  });
}

const movieId = process.argv[2];
printMovieCharacters(movieId);

