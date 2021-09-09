import numpy as np


def grading_function(body: dict) -> dict:
    """
    Function used to grade a student response.
    ---
    The handler function passes only one argument to grading_function(),
    which is a dictionary of the structure of the API request body
    deserialised from JSON.

    The output of this function is what is returned as the API response
    and therefore must be JSON-encodable. This is also subject to
    standard response specifications.

    Any standard python library may be used, as well as any package
    available on pip (provided it is added to requirements.txt).

    The way you wish to structure you code (all in this function, or
    split into many) is entirely up to you. All that matters are the
    return types and that grading_function() is the main function used
    to output the grading response.
    """

    try:
        res = np.array(body["response"], dtype=np.float32)
    except Exception as e:
        return {
            "error": {
                "culprit": "user",
                "description": f"Failed to parse response using `np.array` [{repr(e)}]",
            }
        }

    try:
        ans = np.array(body["answer"], dtype=np.float32)
    except Exception as e:
        return {
            "error": {
                "culprit": "author",
                "description": f"Failed to parse response using `np.array` [{repr(e)}]",
            }
        }

    rtol = body.get("params", {}).get("rtol", 0)
    atol = body.get("params", {}).get("atol", 0)

    is_correct = np.allclose(res, ans, rtol=rtol, atol=atol)

    # TODO: If incorrect, could compute which cells are, and return as feedback

    return {"is_correct": is_correct}
