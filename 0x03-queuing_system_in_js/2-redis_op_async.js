import { createClient, print } from 'redis';
import util from 'util';

const client = createClient();

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  console.log(await util.promisify(client.GET).bind(client)(schoolName));
}


client
  .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', async () => {
    console.log('Redis client connected to the server');
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
  });
