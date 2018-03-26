import { DynamoDB } from 'aws-sdk'

export default (event, context, callback) => {
  const dynamo = new DynamoDB()

  return Promise.resolve()
    .then(() => {
      return dynamo
        .scan({
          TableName: process.env.DYNAMO_TABLE_NAME,
        })
        .promise()
    })
    .then(({ Items: items }) => {
      return items.reduce((acc, item) => {
        acc[item.cid.S] = {
          cookie_count: Number(item.count.N)
        }

        return acc
      }, {})
    })
    .then(total => {
      return callback(null, { statusCode: 200, body: JSON.stringify({ total }) })
    })
    .catch(err => {
      return callback(null, { statusCode: 500, body: JSON.stringify({ err }) })
    })
}
