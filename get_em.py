import difflib
import pandas as pd

class NameGetter:
    def __init__(self):
        self.names = pd.read_csv("baby-names.csv")['name'].tolist()

    def getmatch(self, s):
        return difflib.get_close_matches(s, self.names, n=1)[0]