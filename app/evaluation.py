import numpy as np


def evaluation_function(response, answer, params) -> dict:
    """
    Function used to evaluate a student response.
    ---
    The handler function passes only one argument to evaluation_function(),
    which is a dictionary of the structure of the API request body
    deserialised from JSON.

    The output of this function is what is returned as the API response
    and therefore must be JSON-encodable. This is also subject to
    standard response specifications.

    Any standard python library may be used, as well as any package
    available on pip (provided it is added to requirements.txt).

    The way you wish to structure you code (all in this function, or
    split into many) is entirely up to you. All that matters are the
    return types and that evaluation_function() is the main function used
    to output the grading response.
    """

    try:
        res = np.array(response, dtype=np.float32)
    except Exception as e:
        raise SyntaxError(
            f"Failed to parse response using `np.array` [{repr(e)}]")

    try:
        ans = np.array(answer, dtype=np.float32)
    except Exception as e:
        raise SyntaxError(
            f"Failed to parse answer using `np.array` [{repr(e)}]")

    rtol = params.get("rtol", 0)
    atol = params.get("atol", 0)

    is_correct = np.allclose(res, ans, rtol=rtol, atol=atol)

    # TODO: If incorrect, could compute which cells are, and return as feedback

    return {"is_correct": is_correct}
