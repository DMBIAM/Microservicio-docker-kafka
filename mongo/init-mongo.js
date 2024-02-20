// init-mongo.js

// Connect to the "logs" database (will create the database if it does not exist)
var db = db.getSiblingDB('logs');

// Create the "events" collection in the "logs" database (if it does not exist)
db.createCollection('events');