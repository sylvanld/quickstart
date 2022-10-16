from re import Pattern
import sys, tty, termios
from typing import Callable, List

from quickstart.models import Context, InputVariable, VariableType

def input_list():
    text_in = None
    l = []
    k = 0
    while text_in != "":
        text_in = input("item[%s]: " % k)
        if text_in != "":
            l.append(text_in)
        k += 1
    print(l)
    return l


def validate_string(string: str, regex: Pattern = None, choices: str = None):
    if regex and not regex.match(string):
        raise ValueError("%s does not match pattern: %s" % (string, regex))
    if choices and string not in choices:
        raise ValueError("wrong value: %s. you must choose from: %s" % (string, ', '.join(choices)))  

def input_string(prompt: str, validator: Callable = None) -> str:
    string = input("Input string value for variable %s: " % prompt)
    if validator is not None:
        validator(string)
    return string

def get_char():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        if ch == "\x03":
            raise KeyboardInterrupt
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    
    return ch

def prompt_variable(variable: InputVariable):
    if variable.prompt is None:
        variable.prompt = "Value for variable %s" % (variable.name)
    
    if variable.type in (VariableType.FLOAT, VariableType.INTEGER, VariableType.STRING):
        value = input(variable.prompt + " (%s) : " % variable.type.value)
    elif variable.type is VariableType.LIST:
        print(variable.prompt)
        value = input_list()
    elif variable.type is VariableType.BOOLEAN:
        print(variable.prompt + " ([t]rue/[f]alse) : ")
        char = get_char()
        if char == "t":
            value = True
        elif char == "f":
            value = False
        else:
            raise ValueError("Invalid input! Must be t or f")
      
    return value


def prompt_missing_variables(variables: List[InputVariable], context: Context = None):
    values = {}
    for variable in variables:
        value = None
        if context is not None:
            value = context.variables.get(variable.name)
        if value is None:
            value = prompt_variable(variable)
        values[variable.name] = value
    return values