#!/usr/bin/node

import { createClient } from 'redis';

const subscriber = createClient();

subscriber
  .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'));

subscriber
  .SUBSCRIBE('holberton school channel')

subscriber
  .on('message', (channel, message)=> {
    if (message === 'KILL_SERVER') {
      subscriber.unsubscribe();
      subscriber.quit();
    }
    console.log(message);
  });
