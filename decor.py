import logging
from pprint import pprint
import datetime


def parametrized_decor(path):
    def decorator(function_to_decorate):
        def a_wrapper_accepting_arguments(*args, **kwargs):
            current_datetime = datetime.datetime.now()
            function_name = function_to_decorate.__name__
            result = function_to_decorate(*args, **kwargs)
            logging.basicConfig(
                level=logging.DEBUG,
                filename="mylog.log",
                format=f"{current_datetime} -  %(levelname)s - {args, kwargs} - {function_name} - {result} "
                )

            logging.info(a_wrapper_accepting_arguments)
            return function_to_decorate(*args, **kwargs)
        return a_wrapper_accepting_arguments
    return decorator

