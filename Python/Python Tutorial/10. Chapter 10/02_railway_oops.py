# import pandas as pd

pd.DataFrame()
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

sachinApplication = RailwayForm()
sachinApplication.name = "Sachin"
sachinApplication.train = "Rajdhani Express"
sachinApplication.printData()