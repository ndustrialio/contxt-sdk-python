# Worker

We define a worker to be a machine client that operates on a schedule. This client also has associated scopes and roles to restrict how it can communicate with a Contxt API.

## Machine Client

Within Contxt, a machine client is identified by a unique client id and secret pair. These credentials are generated for you when creating a service in Contxt. For more detailed information about this authentication flow, see [here](https://contxt.readme.io/docs/machine-to-machine-authentication).

## Base Worker Class

Our SDK provides a `BaseWorker` class to help abstract the authentication process between a machine client and a Contxt API. Upon instantation, the class will look for your machine credientials in the environment variables `CLIENT_ID` and `CLIENT_SECRET`, and then store this pair as the attribute `auth`. Next, your worker's business logic is defined in the `do_work()` method. If we need to make requests to a Contxt API here, we simply inject our credentials when instantiating the service class (i.e. `FacilitiesService(self.auth)`). Now, that class handles generating, sending, and refreshing your JWT to authenticate requests to that API.

For a more concrete example, see [worker.py](examples/worker.py).
