#!/usr/bin/node
// prints the number of movies where the character Wedge Antilles is present

const args = process.argv;
let reqURL = args[2];
let request = require('request');
request(reqURL, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    let j_string = JSON.parse(body);
    let results = j_string['results'];
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      let chars = (results[i]['characters']);
      for (let j = 0; j < chars.length; j++) {
        let c_dig = chars[j].endsWith('18/');
        if (c_dig) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
