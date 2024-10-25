import pandas as pd

#Pre-Proccessing 

#Converted all data from pdf file into excel
df = pd.read_excel("./TT_Changes.xlsx") 

#Setting SlNo column as index
df["SlNo"] = df["SlNo"].astype(int) 
df.set_index("SlNo", inplace=True)

#Converting String data in Existing and New columns into a list of prof's names
df["Existing"] = df["Existing"].apply(lambda profs: profs.split(', '))
df["New"] = df["New"].apply(lambda profs: profs.split(', '))

#Columnwise parsing:
def columnwise_parsing():
    df.to_json('./TT_Changes_ColumnWise.json', indent=4)


#Rowwise parsing:
def rowwise_parsing():
    obj = []

    for i in range(0, len(df)):
        info_dict = {}
        for col in df.columns:
            info_dict[col] = df.iloc[i][col]
        obj.append(info_dict)

    sorted_series = pd.Series(obj)

    sorted_series.to_json("./TT_Changes_RowWise.json", indent = 4)

#Taking input for preferred method of parsing: 
def parse_file():
    response = input("How do you want your timetable file parsed? Row-wise or Column-wise or both (r/c/b): ")

    if response == "r":
        rowwise_parsing()
        print("Parsed row-wise.")
    elif response == "c":
        columnwise_parsing()
        print("Parsed column-wise.")
    elif response == "b":
        rowwise_parsing()
        columnwise_parsing()
        print("Parsed both ways.")
    else:
        print("Enter a valid option.")
        parse_file()

parse_file()