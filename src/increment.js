import { DynamoDB } from 'aws-sdk'

export default (event, context, callback) => {
  const queryParams = event.queryStringParameters || {}

  const yourCookie = queryParams.my_cookie || 'no_cookie'

  const dynamo = new DynamoDB()

  return Promise.resolve()
    .then(() => {
      return dynamo
        .getItem({
          Key: {
            cid: {
              S: yourCookie
            }
          },
          TableName: process.env.DYNAMO_TABLE_NAME,
        })
        .promise()
    })
    .then(({ Item: item }) => {
      const currentCount = Number(item.count.N)

      return currentCount + 1
    })
    .catch(() => 1) // errors mean that the item doesn't exist
    .then(newCount => {
      return dynamo
        .putItem({
          Item: {
            cid: {
              S: yourCookie
            },
            count: {
              N: JSON.stringify(newCount) // because Amazon :rolling_eyes:
            },
          },
          TableName: process.env.DYNAMO_TABLE_NAME,
        })
        .promise()
    })
    .then(resp => {
      return callback(null, { statusCode: 200, body: JSON.stringify(resp) })
    })
    .catch(err => {
      return callback(null, { statusCode: 500, body: JSON.stringify(err) })
    })
}
