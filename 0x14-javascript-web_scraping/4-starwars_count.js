#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function(error, response, body){
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results|| [];
    const filmWithWedge = films.filter(function(film) {
      return film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
    });
    console.log(filmWithWedge.length);
  }
})

