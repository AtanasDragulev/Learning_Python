import pandas
import csv

squirrels = {}

data = pandas.read_csv("Squirrel_Data.csv")

color, count = "grey", len(data[data["Primary Fur Color"] == "Gray"])
squirrels[0] = {"Fur Color": color, "count": count}
color, count = "red", len(data[data["Primary Fur Color"] == "Cinnamon"])
squirrels[1] = {"Fur Color": color, "count": count}
color, count = "black", len(data[data["Primary Fur Color"] == "Black"])
squirrels[2] = {"Fur Color": color, "count": count}
squirrels = pandas.DataFrame.from_dict(squirrels, orient="index")
squirrels.to_csv("squirrels.csv")
