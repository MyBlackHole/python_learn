import logging
import time

from jaeger_client import Config, SpanContext

if __name__ == "__main__":
    log_level = logging.DEBUG
    logging.getLogger("").handlers = []
    logging.basicConfig(format="%(asctime)s %(message)s", level=log_level)

    # config = Config(
    #     config={ # usually read from some yaml config
    #         'sampler': {
    #             'type': 'const',
    #             'param': 1,
    #         },
    #         'logging': True,
    #     },
    #     service_name='your-app-name',
    #     validate=True,
    # )

    config = Config(
        config={  # usually read from some yaml config
            "sampler": {
                "type": "const",
                "param": 1,
            },
            "local_agent": {
                "reporting_host": "172.17.0.2",
                "reporting_port": "6831",
            },
            "logging": True,
        },
        service_name="BlackHole4",
        validate=True,
    )

    # this call also sets opentracing.tracer
    tracer = config.initialize_tracer()

    span = tracer.start_span("black4")
    span.log_kv({"input_event": "B", "dict": "ok"})

    child_span = tracer.start_span("Hole4", child_of=span)
    child_span.log_kv({"event": "H"})
    child_span.finish()

    span.log_kv({"output_event": "B", "dict": "ok"})
    span.finish()

    time.sleep(
        2
    )  # yield to IOLoop to flush the spans - https://github.com/jaegertracing/jaeger-client-python/issues/50
    tracer.close()  # flush any buffered spans
