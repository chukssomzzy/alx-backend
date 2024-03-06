#!/usr/bin/npm run dev

import kue from 'kue';

const blackList = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blackList.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }
  job.progress(50, 100);
  done();
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

const jobQueue = kue.createQueue();

jobQueue.process('push_notification_code_2', 2,
  (job, done) => sendNotification(job.data.phoneNumber, job.data.message, job, done));
