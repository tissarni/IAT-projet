import os
import plotly.express as px
import pandas as pd
from sys import argv


class logAnalysis:
    def __init__(self, file: str):
        self.file = file
        self.values = []

    def printCurves(self):
        df = pd.read_csv(self.file)
        fig = px.scatter(x=df["episode"], y=df["score"])
        fig.show()


if __name__ == '__main__':
    log = logAnalysis(str(argv[1]))
    log.printCurves()