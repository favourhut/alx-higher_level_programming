#!/usr/bin/node
const variable = require('variable');
variable.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
