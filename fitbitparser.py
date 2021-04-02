import json 
import csv 
import requests

# Make HTTP GET request for intra day data  
# Open JSON file and load the data from the request

#month_range
#day_range  or list of dates to collect 

month = '08'

for day in range(25,32):
    print("Day:",day)

    fit_url = f"https://api.fitbit.com/1/user/-/activities/steps/date/2019-{month}-{day}/2019-{month}-{day}.json"

    if day < 10:
        fit_url = f"https://api.fitbit.com/1/user/-/activities/steps/date/2019-{month}-0{day}/2019-{month}-0{day}.json"

    bearer = '' # enter bearer here
    
    headers = {'Authorization': f'Bearer {bearer}'}

    response = requests.get(fit_url, headers= headers)

    pdata = response.json()

    

    # with open('/Users/danmedina/Documents/Fitbit Parser/Steps_06212019.json') as json_file: 
    #     data = json.load(json_file) 
    
    fitbit_data = pdata['activities-steps-intraday']['dataset'] 

    #print(fitbit_data) # verifies that the json loaded correctly

    #Open a CSV file for writing 
    data_file = open(f'/Users/danmedina/Documents/Fitbit Parser/NYIT001_Steps_{month}{day}2019.csv', 'w') 

    # create the csv writer object
    csv_writer = csv.writer(data_file) 
    
    # Count variable used to add the headers for the Data file
    count = 0
    
    for row in fitbit_data: 
        if count == 0: 
            header = row.keys() 
            csv_writer.writerow(header) 
            count += 1
        
        # Writing data of CSV file 
        csv_writer.writerow(row.values()) 
    
    data_file.close()