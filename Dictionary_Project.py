import csv

result = []
user_search_zip = input("Please enter the five digit zip code you wish to search.  ")
zip_length = len(user_search_zip)

while zip_length != 5:
    if zip_length > 5:
        print("Zip code too long.  Please enter a zip code with only five digits.")
        
    else:
        print("Zip code too short.  Please enter a zip code with five digits.")
    
    user_search_zip = input("Please enter the five digit zip code you wish to search.  ")
    zip_length = len(user_search_zip)

with open('tri_water.csv') as trifile:
    dreader = csv.DictReader(trifile)
    result = [entry for entry in dreader if entry['ZIP_CODE'] == user_search_zip] 
    

def print_result(result):
    if not result:
        print (f"No results located for the zip code: {user_search_zip}.  Congratulations on not being poisioned!")
    else:
        print( "Year   Carcinogen   Chemical Name") 
        for entry in result:
            print (entry['REPORTING_YEAR'],"     ", entry['CARCINOGEN'], "     ", entry['CHEM_NAME'] )

print_result(result)

#Summary line that gives total instances for distinct chemicals, summary line showing total instances per year.
#count of carcinogen and non carincogen instances per year

