#!/usr/bin/node
import kue from 'kue';
import { assert } from 'chai';

import createPushNotificationsJobs from './8-job';

const jobQueue = kue.createQueue();

before(() => jobQueue.testMode.enter());
afterEach(() => jobQueue.testMode.clear());


after(() => jobQueue.testMode.exit())

describe('Test createPushNotificationsJobs', () => {
  it('jobs passed as string', () => {
    assert.throws(() => createPushNotificationsJobs('Jobs not an array', jobQueue), 'Jobs is not an array');
  })

  it('jobs passed as object', () => {
    assert.throws(() => createPushNotificationsJobs({phoneNumber: '42342342423424', message: 'your verification code is 1245'}, jobQueue), 'Jobs is not an array');
  })

  it('jobs passed as a number', () => {
    assert.throws(() => createPushNotificationsJobs(123424234, jobQueue), 'Jobs is not an array');
  })

  it('jobs passed as an empty array', () => {
    assert.ok(() => createPushNotificationsJobs([], jobQueue));
    assert.equal(jobQueue.testMode.jobs.length, 0);
  })

  it('jobs passed without the queue', () => {
    assert.ok(() => createPushNotificationsJobs([{phoneNumber: '12343456789', message: 'send verification 1234'}]));
    assert.equal(jobQueue.testMode.jobs.length, 0);
  })

  it('jobs with one job and queue', () => {
    const oneJob = [{phoneNumber: '123456789', message: 'send verification 1234'}];
    createPushNotificationsJobs(oneJob, jobQueue);
    assert.equal(jobQueue.testMode.jobs.length, 1);
    assert.deepEqual(jobQueue.testMode.jobs[0].data, oneJob[0]);
  })

  it('jobs without a queue', () => {
    const oneJob = [{phoneNumber: '123456789', message: 'send verification 1234'}];
    assert.throws(() => createPushNotificationsJobs(oneJob), TypeError);
  })
})
