import pandas as pd


#Clean up the txt data so python can read it, catagorize it, and add it to a dictionary

def parse_line(line):
    cleaned_line = line.strip()     #removes invisible \n line that is at the end of a text file such as 5.1|3.5|1.4|0.2|Iris-setosa\n"

    fields = cleaned_line.split('|')        #removes the | separators and creates a list with individual elements

    sepal_length = float(fields[0])     #turns the first 4 element into floating numbers and fields that can be called. Python thinks its a string/
    sepal_width = float(fields[1])
    petal_length = float(fields[2])
    petal_width = float(fields[3])
    species = fields[4]     #We keep the last field a string because it's the name of the spieces of flower

    parsed_line = [sepal_length, sepal_width, petal_length, petal_width, species]

    return parsed_line


def add_to_dict(parsed_line, data_dict):
    if len(parsed_line) != len(data_dict):      #"does the row being added to the dictionary have the same # of items as the dictionary has columns?"
        raise ValueError("number of fields does not match dictionary keys.")      #If not, tell user


#if there are no issues, we take the row of data we want to add and put them in the correct column of our dictionary
    keys = list(data_dict.keys())

    for i in range(len(keys)):
        key = keys[i]
        value = parsed_line[i]
        data_dict[key].append(value)

#The next function will take the iris.txt file, one line at a time, and build the dictionary using the two previous functions we created
def load_data(filename):
    data_dict = {                           #data_dict creates an empty dictionary with the fields created above
        "sepal_length": [],
        "sepal_width": [],
        "petal_length": [],
        "petal_width": [],
        "species": []
    }

    with open(filename, "r") as file:
        for line in file:
            if line.strip() == "":      #If the function finds an empty line, it skips. This is a common issue with raw data
                continue

            parsed_line = parse_line(line)
            add_to_dict(parsed_line, data_dict)     #this adds the cleaned up line to the dictionary

    dataframe = pd.DataFrame(data_dict)         #this coverts the dictionary to a panda we can use to look at the data

    return dataframe


#The next function will allow us to get a measurement average for a specific species, and a specific column like length or width

def species_mean(data, species, measurement):
    species_rows = data[data["species"] == species]

    measurement_values = species_rows[measurement]

    average = measurement_values.mean()

    return average


