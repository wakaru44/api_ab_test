
# A/B Testing API

A ultra simplistic RESTfake (Rest in your own grave) API for a dirty little experiment

TODO'S:

- termina los metodos para validar input y demas
- empezar a pensar en a donde mandar los mensajes.

## Calls:

#### /event

The main call to register an event. 
In this version, we are going to use the url as a path to send details.

The format of the URL should be something like 

`/event/GUID/109201390/client_normal/login_button`

having this components:

- SessionID: GUID (or a string for the purpose of this demo)
- Timestamp: Int. The unix timestamp in the client
- Client Version: String. Something to identify the version/kind/variation of the client
- Item: String. The thing that the user has touched. 

In this order, and validating a bit.
