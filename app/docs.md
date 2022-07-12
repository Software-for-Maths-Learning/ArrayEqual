# ArrayEqual

Evaluation function checks if the supplied response and answer arrays are within the optionally supplied tolerances. This is based on the [numpy.allclose](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html) function. Numpy is a dependancy for this function, but it means that arrays of any shape (regular) can be compared efficiently.

## Inputs
Valid params include `atol` and `rtol`, which can be used in combination, or alone. (just like the [`IsSimilar`](https://github.com/lambda-feedback/IsSimilar) grading function)

```json
{
  "response": "<array>",
  "answer": "<array>",
  "params": {
    "atol": "<number>",
    "rtol": "<number>"
  }
}
```

_Note:_ `response` and `answer` arrays are parsed using `np.array(dtype=np.float32)`, any errors this causes are returned and the comparison fails.

### `atol`
Absolute tolerance parameter

### `rtol`
Relative tolerance parameter

## Outputs 

## Examples