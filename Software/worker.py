import requests
from typing import Dict, Any

## Worker.py -- 
# the worker is responsible for executing the actions defined in the workflow
# this level of abstraction is where the structured procedure steps are mapped to the actual actions
# these actions are defined as functions, each corrisponding to a unique action. 
# these will not be the final translation of the action and will rely on mapped gcode and macro calls outlined
# in the requestlib.py file.

# Import the ReactionStep and ProcedureStep from workflow.py
from workflow import ReactionStep, ProcedureStep, steps

# Define functions for each action
def solv(vial: str, solvent: int, vol: float, rate: float):
    return call_api("solv", {"vial": vial, "solvent": solvent, "vol": vol, "rate": rate})

def inject(vial: str, vol: float, rate: float):
    return call_api("add", {"vial": vial, "vol": vol, "rate": rate})

def draw(vial: str, vol: float, rate: float):
    return call_api("draw", {"vial": vial, "vol": vol, "rate": rate})

def temp(vial: str, val: float, rate: float):
    return call_api("temp", {"vial": vial, "val": val, "rate": rate})

def filter(vial: str, vol: float, solvent: int):
    return call_api("filter", {"vial": vial, "vol": vol, "solvent": solvent})

def seal(vial: float, state: bool):
    return call_api("seal", {"vial": vial, "state": state})

def move(vial: str, location: str):
    return call_api("move", {"vial": vial, "location": location})

# Map action strings to functions
action_map = {
    "solv": solv,
    "add": add,
    "temp": temp,
    "filter": filter,
    "seal": seal,
    "move": move
}

## workflow.py should be brought in here and the steps should be iterated over with the actions being called. we should define this in the main as a worker.start({workflow})