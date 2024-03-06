import { createClient, print } from 'redis';

client = createClient()

client
  .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', (err) => console.log('Redis client connected to the server'))

const holbertonSchool = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Pari': 2
}

function setHset(skey, obj) {
  Object(obj).entries.map((key, val) => client.hset)
}


