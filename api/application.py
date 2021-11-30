from api.database import DBDriver
from api.controller import Controller
from api.model import Model
from api.view import View

class Application:
    controller = Controller(Model(), View())