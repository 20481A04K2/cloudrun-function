import json
from flask import Request

def main(request: Request):
    """
    Simple Cloud Run Function (Gen2)
    """

    if request.method == "POST":
        request_json = request.get_json(silent=True)

        if request_json and "name" in request_json:
            name = request_json["name"]
            return {
                "status": "success",
                "message": f"Hello {name}!"
            }

        return {
            "status": "error",
            "message": "No name provided"
        }, 400

    return {
        "status": "success",
        "message": "Cloud Run Function is working 🚀"
    }
