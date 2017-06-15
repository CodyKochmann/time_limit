# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-05-17 13:15:56
# @Last Modified 2017-02-06
# @Last Modified time: 2017-06-15 15:32:01

"""

This wrapper enables a timeout error flag with python functions.

import this file with:

    from timeout import timeout

use this with:

    @timeout(seconds_to_limit_next_line_to)
    def function_to_run():
        print "this needs to run faster than the line before this funciton definition"

if you want a default output instead of an error, use:

    @timeout(seconds, default_output)
"""

from __future__ import print_function
from functools import wraps
from os import strerror
from errno import ETIME
from signal import alarm, signal, SIGALRM


class TimeoutError(Exception):
    """ custom timeout exception to be thrown if time limit is exceeded """
    pass


def timeout(seconds=10, default_output='default_output'):
    """ function wrapper that limits the amount of time it has to run
    optional args:
        seconds - how long it has until the function times out
        default_output - what will be returned instead of an error
    """
    def decorator(func):
        def _handle_timeout(signum, frame):
            """ throw the custom TimeoutError if called """
            raise TimeoutError(strerror(ETIME))

        def wrapper(*args, **kwargs):
            """ main wrapper for the error """
            # set up the propper error signal
            signal(SIGALRM, _handle_timeout)
            # set the time the function has to run
            alarm(seconds)
            try:
                result = func(*args, **kwargs)
            except TimeoutError:
                if default_output == 'default_output':
                    raise
                else:
                    result = default_output
            finally:
                # cancel the timer
                alarm(0)
            return result

        return wraps(func)(wrapper)
    return decorator

if __name__ == '__main__':
    #============================================================
    # with default output, the invocation is a lot cleaner
    #============================================================
    @timeout(2, default_output='no html found')
    def get_link(url):
        while 1:
            x=5+1
        return 'some_html'

    print(get_link('whatever'))

    #============================================================
    # without default output, more logic is needed when calling
    #============================================================
    @timeout(2)
    def get_link(url):
        while 1:
            x=5+1
        return 'some_html'

    try:
        html = get_link('whatever')
    except TimeoutError:
        html = 'no html found'
    print(html)
