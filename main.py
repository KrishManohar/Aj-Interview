import os
import re
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from mangum import Mangum
import random

stage = 'staging'
openapi_prefix = f"/{stage}"

app = FastAPI(openapi_prefix=openapi_prefix)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

python_json = [
    "Python was named after Monty Python's Flying Circus.",
    "Python's philosophy: 'Readability counts'.",
    "Python developers 'pythonize' their problems.",
    "The Zen of Python: Beautiful code is sacred.",
    "Python is beloved by data scientists.",
    "Pythonistas embrace 'snake_case'.",
    "'Lambda' functions in Python are like ninjas.",
    "Python doesn't need semicolons; they roam free!",
    "Python developers enjoy 'Java' (the drink).",
    "Python: Where you understand recursion or exceed max recursion depth.",
    "Python's 'antigravity' module lifts spirits.",
    "Python libraries: An expanding endless universe!",
    "'Import this' reveals the Zen of Python.",
    "Python's 'magic methods' make code elegant.",
    "Python's 'try-except': Code parachutes!",
    "The 'GIL' ensures code plays nice and not too fast.",
    "Python's 'turtle' module: Digital pet turtle!",
    "Python's errors whisper but never pass silently.",
    "Python's 'virtual environments': Code personalities!",
    "Python detectives love solving code mysteries in 'spyder'.",
    "Careful! Python's 'TypeError' can break hearts.",
    "Python's 'pyjokes' library brings laughter to code.",
    "'None': Python's answer to everything.",
    "Python's 'asyncio': Juggling tasks like circus performers.",
    "Syntax, the Python developer's favorite snake.",
    "Python developers add 'pip' to their code recipes.",
    "Python's 'pickle': Pickling objects, no jars involved.",
    "Python developers love the powerful 'pandas' library.",
    "Python developers 'raise' exceptions, not curses.",
    "Python developers travel with the 'dict'ionary!"
]


@app.get("/index")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/python")
async def get_answer():
    """
    Get Random Python Response
    ---
    summary: Retrieve a random Python response.
    description: This endpoint returns a random Python response from a pre-defined list of responses.
    """
    random_python_response = random.choice(python_json)
    return random_python_response


@app.get("/reverse/{name}")
async def reverse_name(name: str = None):
    """
    Reverse Name Endpoint
    ---
    summary: Reverse the provided name and return the letter count.
    description:
    This endpoint takes a string containing a name, validates if it consists of letters only and is not empty,
      calculates the letter count of the name, and returns the reversed name along with the letter count.
    """

    if not re.match(r"^[A-Za-z]+$", name):
        raise HTTPException(status_code=400, detail="Name must contain only letters.")

    letter_count = len(name)

    # for slicing, and the `-1` inside the square brackets indicates the step value.In this case, `-1` means that it
    # will iterate the string in reverse order.
    reversed_name = name[::-1]
    response_data = {"letterCount": letter_count, "reversedName": reversed_name}
    return JSONResponse(content=response_data)


lambda_handler = Mangum(app)