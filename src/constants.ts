export const questions = [
  {
    type: 'input',
    name: 'projectName',
    message: 'What is the name of your project?'
  },
  {
    type: 'confirm',
    name: 'useRest',
    message: 'Will use Rest?',
    default: true,
  },
  {
    type: 'confirm',
    name: 'useGraphql',
    message: 'Will use GraphQL?',
    default: false,
  },
  {
    type: 'confirm',
    name: 'useKafka',
    message: 'Will use Kafka?',
    default: false,
  },
  {
    type: 'confirm',
    name: 'useGrpc',
    message: 'Will use gRPC?',
    default: false,
  },
  {
    type: 'confirm',
    name: 'useRabbitMQ',
    message: 'Will use RabbitMQ?',
    default: false,
  },
  {
    type: 'confirm',
    name: 'useMongoDB',
    message: 'Will use MongoDB?',
    default: false,
  },
  {
    type: 'confirm',
    name: 'usePostgreSQL',
    message: 'Will use PostgreSQL?',
    default: false,
  },
]
