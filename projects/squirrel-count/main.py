import pandas

data = pandas.read_csv('data/central_park.csv')

grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print(f"Grey: {grey_squirrels}")
print(f"Red: {red_squirrels}")
print(f"Black: {black_squirrels}")

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("data/squirrel_count.csv")