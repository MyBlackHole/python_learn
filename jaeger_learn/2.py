import logging
from jaeger_client import Config
import time


def say_hello(hello_to):
    with tracer.start_span('say-hello') as span:
        span.set_tag('hello-to', hello_to)
        hello_str = format_string(span, hello_to)
        print_hello(span, hello_str)


def format_string(root_span, hello_to):
    with tracer.start_span('format', child_of=root_span) as span:
        hello_str = 'Hello, %s!' % hello_to
        span.log_kv({'event': 'string-format', 'value': hello_str})
        return hello_str


def print_hello(root_span, hello_str):
    with tracer.start_span('println', child_of=root_span) as span:
        print(hello_str)
        span.log_kv({'event': 'println'})


def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    # config = Config(
    #     config={
    #         'sampler': {
    #             'type': 'const',
    #             'param': 1,
    #         },
    #         'logging': True,
    #     },
    #     service_name=service,
    # )

    config = Config(
        config={  # usually read from some yaml config
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'local_agent': {
                'reporting_host': '172.17.0.2',
                'reporting_port': '6831',
            },
            'logging': True,
        },
        service_name='BlackHole2',
        validate=True,
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()


tracer = init_tracer('hello-world')
say_hello("server2")
time.sleep(2)
tracer.close()
