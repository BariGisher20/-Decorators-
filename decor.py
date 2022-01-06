import logging
import datetime
import os


def decorator(function_to_decorate):
    def a_wrapper_accepting_arguments(*args, **kwargs):
        current_datetime = datetime.datetime.now()
        function_name = function_to_decorate.__name__
        result = function_to_decorate(*args, **kwargs)
        logging.basicConfig(
            level=logging.DEBUG,
            filename="mylog.log",
            format=f"{current_datetime} -  %(levelname)s - {args, kwargs} - {function_name} - {result} - {os.path.abspath('mylog.log')}")

        logging.info(a_wrapper_accepting_arguments)
        return function_to_decorate
    return a_wrapper_accepting_arguments

