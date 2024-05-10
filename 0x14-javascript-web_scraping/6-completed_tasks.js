#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) { console.error(error); }
  const todos = JSON.parse(body);
  try {
    const userTasks = {};
    todos.forEach((todo) => {
      if (todo.completed) {
        if (userTasks[todo.userId]) {
          userTasks[todo.userId]++;
        } else {
          userTasks[todo.userId] = 1;
        }
      }
    });
    console.log(userTasks);
  } catch (error) {
    console.error(error);
  }
});
