import os

class Generator:
    def __init__(self):
        print("Init")

    def create(self, folder):
        folder = os.path.abspath(folder)
        if os.path.isdir(folder):
            raise Exception(f"This folder already exists, not overwriting it: {folder}")
        if not os.path.isdir(os.path.dirname(folder)):
            raise Exception(f"Parent folder does not exist, not creating it: {folder}")
        
