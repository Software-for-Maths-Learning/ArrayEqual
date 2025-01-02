# ArrayEqual

This function is used to compare two number arrays/vectors/matrices, provided absolute and/or relative tolerance parameters `rtol` and `atol`. This is carried out using the [numpy.allclose](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html) function.

If the answer is not an array of numbers an exception is raised. If the response is not an array of numbers, a feedback message that informs the user that only numbers are accepte will be generated.

### Optional parameters

There is one optional parameter: `feedback_for_incorrect_response`.

## `feedback_for_incorrect_response`
All feedback for all incorrect responses will be replaced with the string that this parameter is set to.