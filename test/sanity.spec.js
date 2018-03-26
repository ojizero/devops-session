require('./setup')

describe('It Works', function () {
  it('Successfully requires module', function () {
    const lambda = () => require('../src').countAll

    expect(lambda).to.not.throw()
  })

  it('Work hopefully', function () {
    const lambda = require('../src').countAll
    const event = require('./fixtures/count-all-event.json')

    const response = executeLambda(lambda, event)

    // expect(response)
      // .to.be.an('object')
      // .and.to.have.all.keys('statusCode', 'body')
      // .and.to.have.nested.key('body.total')
  })
})
