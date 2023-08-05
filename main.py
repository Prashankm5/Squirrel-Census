import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrels = data[data['Primary Fur Color'] == 'Gray']
red_squirrels = data[data['Primary Fur Color'] == 'Cinnamon']
black_squirrels = data[data['Primary Fur Color'] == 'Black']
gray_squirrels_count = len(gray_squirrels)
red_squirrels_count = len(red_squirrels)
black_squirrels_count = len(black_squirrels)

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
print(df)

df.to_csv("squirrel_count.csv")

