const redis = require('redis');
const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool (schoolName, value) {
  if (typeof value === 'object') {
    value = JSON.stringify(value);
  }
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue (schoolName) {
  client.get(schoolName, (error, reply) => {
    if (error) {
      console.log(error.message);
    }
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
