import numpy as np
from evaluation_function_utils.errors import EvaluationException


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

    answer_ok = process_element(answer)
    if not answer_ok:
        raise Exception("Answer has empty fields.")
    response_ok = process_element(response)
    if not response_ok:
        return {
            "is_correct": False,
            "feedback": "Response has empty fields."
        }

    try:
        res = np.array(response, dtype=np.float32)
    except Exception as e:
        raise EvaluationException(
            f"Failed to parse user response",
            detail=repr(e)
        )

    try:
        ans = np.array(answer, dtype=np.float32)
    except Exception as e:
        raise EvaluationException(
            f"Failed to parse correct answer",
            detail=repr(e)
        )

    rtol = params.get("rtol", 0)
    atol = params.get("atol", 0)

    is_correct = np.allclose(res, ans, rtol=rtol, atol=atol)

    if is_correct is False and params.get("feedback_for_incorrect_response", None) is not None:
        return {
            "is_correct": is_correct,
            "feedback": params["feedback_for_incorrect_response"]
        }

    # TODO: If incorrect, could compute which cells are, and return as feedback
    return {"is_correct": is_correct}

def process_element(element):
    is_ok = True
    if isinstance(element,list):
        for e in element:
            is_ok = process_element(e)
    else:
        if isinstance(element,str):
            element = element.strip()
            if len(element) == 0 or "element" == "undefined":
                is_ok = False
            else:
                element = float(element)
    return is_ok