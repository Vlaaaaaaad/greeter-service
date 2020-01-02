# greeter-service

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/poc-hello-world/greeter-service)

Proof-of-Concept( PoC ) application that returns a greeting. It is indended to be called by another application that composes a "_Greeter name!_" output. For example for "_Hello world!_" this app would be the one providing the "_Hello_".

![Architecture diagram](./docs/hello-world.svg)

## Intended use

The purpose of this application is to be used for microservices tech demos and example implementations of tools.

**It is in no way, shape, or form a reference for best practices, a good example, or a comprehensive anything**. It is a minimal skeleton app with simple logic that can be built around.

For more complex demos see:
- Google Cloud Platform's [microservices-demo](https://github.com/GoogleCloudPlatform/microservices-demo)
- Microsoft's [eShopOnContainers](https://github.com/dotnet-architecture/eShopOnContainers)
- Weaveworks' and Container Solutions' [Sock Shop](https://github.com/microservices-demo/microservices-demo)
- Istio's [BookInfo](https://istio.io/docs/examples/bookinfo/)
- Kubernetes' [Guestbook](https://kubernetes.io/docs/tutorials/stateless-application/guestbook/) 

## Forks

If you extend this application to do something, please create a Pull Request back with a link to your fork. Some ideas are included in the table already

| Fork link | Extras added |
|-----------|--------------|
|           | + [sentry.io](https://sentry.io) |
|           | + [honeycomb.io](https://honeycomb.io) |
|           | + [launchdarkly.com](https://launchdarkly.com) |
|           | + [gremlin.com](https://www.gremlin.com) |
|           | + read greeting from DynamoDB |

## License

This project is provided under the [MIT License](https://github.com/poc-hello-world/greeter-service/blob/master/LICENSE). See [LICENSE](https://github.com/poc-hello-world/greeter-service/blob/master/LICENSE) for more information.
