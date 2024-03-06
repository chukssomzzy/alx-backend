import { createClient, print } from 'redis';

const client = createClient()

client
  .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'))

const skey = 'HolbertonSchool';

const holbertonSchool = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Pari': 2
};

function setHset(skey, obj) {
  for (const [key, val] of Object.entries(holbertonSchool)) {
    client.HSET(skey, key, val, print);
  }
}

setHset(skey, holbertonSchool);
client.HGETALL(skey, (err, val) => console.log(val));
