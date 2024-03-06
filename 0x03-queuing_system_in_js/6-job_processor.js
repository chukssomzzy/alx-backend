#!/usr/bin/node

import kue from 'kue';

const jobQue = kue.createQueue({name: 'push_notification_code'});

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

jobQue.process('push_notification_code', (job) => {
  sendNotification(job.data.phoneNumber, job.data.message);
});
