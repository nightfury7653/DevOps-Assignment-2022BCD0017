db.createCollection('tasks');
db.tasks.createIndex({ "name": 1 }, { unique: true });