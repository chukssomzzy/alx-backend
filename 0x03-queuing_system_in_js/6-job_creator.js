#!/usr/bin/node

import kue from 'kue';

const jobQueue = kue.createQueue({name: 'push_notification_code'});

const jobData = {
  phoneNumber: '+234803846446',
  message: 'Storage Full'
}

const job = jobQueue.create('push_notification_code', jobData)
  .save();

job.on('enqueue', () => console.log(`Notification job created: ${job.id}`))
  .on('complete', () => console.log('Notification job completed'))
  .on('failed attempt', () => console.log('Notification job failed'));
