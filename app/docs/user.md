# ArrayEqual

This function is used to compare two number arrays/vectors/matrices, provided absolute and/or relative tolerance parameters `rtol` and `atol`. This is carried out using the [numpy.allclose](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html) function.

### Optional parameters

There is one optional parameter: `feedback_for_incorrect_response`.

## `feedback_for_incorrect_response`
All feedback for all incorrect responses will be replaced with the string that this parameter is set to.