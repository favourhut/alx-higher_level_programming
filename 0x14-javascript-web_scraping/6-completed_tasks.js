#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const args = process.argv;
let reqURL = args[2];
let request = require('request');
request(reqURL, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    let task = JSON.parse(body);
    let spec = {};
    for (let i = 0; i < task.length; i++) {
      let status = (task[i]['completed']);
      let key = task[i]['userId'].toString();
      if (status) {
        if (spec[key]) {
          spec[key]++;
        } else {
          spec[key] = 1;
        }
      }
    }
    console.log(spec);
  }
});
