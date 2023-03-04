# Backend Home Assignment

## implement a client-server application that will be used by insurance brokers to manage and track their submission records. 
#### The application should consist of:
1. A server exposing a HTTP based API allowing various operations on the submissions book.
2. A command line REPL client to be used by the insurance broker.


## Running 
1. Run the server on docker, follow instructions in `/server/README.md`
2. Run the client, follow instructions in `/client/README.md`

## Things to do before it will be production ready
### OR thing that I would have done it if I had more time
- Add tests
- Export hard coded information into env vars (SERVER_BASE_URL etc.)
- Use a production server for server
- add error handling, Wrap with a few try except, and send more explaining error messages.
- Save the images on external service (S3?) and server them using nginx
- Containerize client and run everything together using docker-compose
