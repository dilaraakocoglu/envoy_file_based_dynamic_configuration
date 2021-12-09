from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return "<h3> WELCOME TO ENVOY PROXY </h3>"

"""@app.route("/v3/discovery:endpoints", methods = ['POST'])
def endpoints():
    route_config = envoy.RouteConfiguration(
        name='EndpointsRouteConfig',
        virtual_hosts=[
            envoy.route.VirtualHost(
                name='endpoints',
                domains=['0.0.0.0'],
                routes=[
                    envoy.route.Route(
                        name='catchall',
                        match=envoy.route.RouteMatch(
                            prefix='/v3/discovery:endpoints'
                        ),
                        direct_response=envoy.route.DirectResponseAction(
                            status=200,
                            body=envoy.core.DataSource(
                                inline_string='Endpoints Config'
                            )
                        )
                    )
                ]
            )
        ]
    )

    response = envoy.DiscoveryResponse(
        version_info='0',
        resources=[
            route_config
        ],
    )
    return json.dumps(response.to_dict(casing=stringcase.snakecase), indent=2)

@app.route("/v3/discovery:clusters", methods = ['POST'])
def clusters():
    route_config = envoy.RouteConfiguration(
        name='ClustersRouteConfig',
        virtual_hosts=[
            envoy.route.VirtualHost(
                name='clusters',
                domains=['0.0.0.0'],
                routes=[
                    envoy.route.Route(
                        name='catchall',
                        match=envoy.route.RouteMatch(
                            prefix='/v3/discovery:clusters'
                        ),
                        direct_response=envoy.route.DirectResponseAction(
                            status=200,
                            body=envoy.core.DataSource(
                                inline_string='Clusters Config'
                            )
                        )
                    )
                ]
            )
        ]
    )

    response = envoy.DiscoveryResponse(
        version_info='0',
        resources=[
            route_config
        ],
    )
    return json.dumps(response.to_dict(casing=stringcase.snakecase), indent=2)

@app.route("/v3/discovery:listeners", methods = ['POST'])
def listeners():
    route_config = envoy.RouteConfiguration(
        name='ListenersRouteConfig',
        virtual_hosts=[
            envoy.route.VirtualHost(
                name='listeners',
                domains=['0.0.0.0'],
                routes=[
                    envoy.route.Route(
                        name='catchall',
                        match=envoy.route.RouteMatch(
                            prefix='/v3/discovery:listeners'
                        ),
                        direct_response=envoy.route.DirectResponseAction(
                            status=200,
                            body=envoy.core.DataSource(
                                inline_string='Listeners Config'
                            )
                        )
                    )
                ]
            )
        ]
    )

    response = envoy.DiscoveryResponse(
        version_info='0',
        resources=[
            route_config
        ],
    )
    return json.dumps(response.to_dict(casing=stringcase.snakecase), indent=2)"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)