#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const result = JSON.parse(body);
    result.characters.forEach(function (actor) {
      request(actor, function (error, response, body) {
        const character = JSON.parse(body);
        if (!error) {
          console.log(character.name);
        }
      });
    });
  }
});
