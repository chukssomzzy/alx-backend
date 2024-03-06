import { createClient, print } from 'redis';

const client = createClient();

client
  .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.hset(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.GET(schoolName, (_err, val) => console.log(val));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
