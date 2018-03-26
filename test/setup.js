process.env.NODE_ENV = 'test'

const chai = require('chai')
const chaiAsPromised = require('chai-as-promised')
const context = require('aws-lambda-mock-context')
const { promisify } = require('util')

const executeLambda = function (lambda, event = {}, contextOptions) {
  const ctx = context(contextOptions)
  return Promise.race([
    promisify(lambda)(event, ctx),
    ctx.Promise,
  ])
}

chai.use(chaiAsPromised)

global.chai = chai
global.expect = chai.expect
global.executeLambda = executeLambda
