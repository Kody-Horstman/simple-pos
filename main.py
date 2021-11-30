from api.application import Application
from api.database import DBDriver
from api.controller import Controller
from api.model import Model
from api.view import View


def main():
    '''Application entry point.'''
    app = Application()
    
    print("Running application...")

if __name__ == '__main__':
    main()