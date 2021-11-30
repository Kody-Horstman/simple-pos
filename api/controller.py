from api.model import Model
from api.view import View

class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
    
