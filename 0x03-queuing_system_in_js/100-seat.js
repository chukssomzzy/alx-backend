#!/usr/bin/node

import utils from 'util';
import { createClient } from 'redis';
import express from 'express';
import kue from 'kue';

let reservationEnabled = true;

const app = express();
const PORT = 1245;
const client = createClient()
  .on('error', (err) => console.log(`Redis connection failed ${err}`))
  .on('connect', () => console.log('Redis server connected'));
const reservationQueue = kue.createQueue();

function reserveSeat(number) {
    client.set('available_seats', parseInt(number));
}

async function getCurrentAvailableSeats() {
  return await utils.promisify(client.GET).bind(client)('available_seats');
}


app.get('/available_seats', async (req, res) => {
  const seatAvailable = await getCurrentAvailableSeats();

  res.status(200).json({numberOfAvailableSeats: seatAvailable});
})

app.get('/reserve_seat', async (req, res) => {
  if (reservationEnabled) {
    const reserveJob = reservationQueue.create('reserve_seat', {'title': `Reserve Seat`})
      .save((err) => {
        if (err) {
          res.status(500).json({"status": "Reservation failed"});
        } else {
          res.status(200).json({"status": "Reservation in process"})
        }
      });

    reserveJob
      .on('complete', () => console.log(`Seat reservation job ${reserveJob.id} completed`))
      .on('failed', (err) => console.log(`Seat reservation job ${reserveJob.id} failed: ${err}`));
  } else {
    res.status(400).json({ "status": "Reservation are blocked" });
  }
})

app.get('/process', async (req, res) => {
  res.status(200).json({ "status": "Queue processing" });
  reservationQueue.process('reserve_seat', async (job, done) => {
    const available_seats = await getCurrentAvailableSeats();

    if (available_seats <= 0) {
      reservationEnabled = false;
      return done(new Error('Not enough seats available'));
    }
    console.log(available_seats);
    reserveSeat(available_seats - 1);
    done();
  })
})

app.listen(PORT, () => {
  reserveSeat(50);
  console.log(`Sever listen on ${PORT}`)
});
