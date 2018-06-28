from functools import wraps


# wraps源代码
def wraps(wrapped,
      assigned = WRAPPER_ASSIGNMENTS,
      updated = WRAPPER_UPDATES):
    return partial(update_wrapper, wrapped=wrapped,
               assigned=assigned, updated=updated)

from functools import update_wrapper