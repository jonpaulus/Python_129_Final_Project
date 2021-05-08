#Burning Question:  Do younger/newer senators (those with less seniority) vote more on the issue and less on partisan lines

import requests, json, matplotlib.pyplot as plt, csv, numpy as np, matplotlib.patches as mpatches
from statistics import mean

#API key for ProPublica is in pro_publica_api.txt and is not uploaded to Git
with open("pro_publica_api.txt") as f:
    pro_publica_key = f.read()

#Sessions of Congress with necessary voting percentage data start at session 101 year 1989 to 1991 and end at current, session 117

#string template for get_congress_session to allow modification of sessions pulled depending on need 
pro_publica_req = 'https://api.propublica.org/congress/v1/{}/senate/members.json'


#This is a wrapper function that requires the pro_publica_req variable, and the parameter is the session of congress that is desired (necessary for the request to work)
# as well as the required header and propublica key required to authenticate the request by propublica
#Required input:  desired session number in range of 101 to 117
#Output Api get request of specified session of Congress 
def get_congress_session(number):
    return requests.get(pro_publica_req.format(number), headers = {"X-API-Key" : pro_publica_key})

def get_CSV_data(response):
    senators = response.json()['results'][0]['members']
    file_name = "Congressional Session " + response.json()['results'][0]['congress'] + ".csv"
    with open (file_name, mode="w", newline="") as csv_file:
        fieldnames = ["last_name", "first_name", "votes_with_party_pct", "votes_against_party_pct", "votes_against_party_pct", "missed_votes_pct"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for senator in senators:
            writer.writerow(senator)

#scatter plot functions
def calculate_senority(senators):
    seniority = [int (senator["seniority"]) for senator in senators]
    maximum = max (seniority)
    return [ maximum - i for i in seniority]

def calculate_votes_with_party(senators):
    return [float(senator["votes_with_party_pct"]) for senator in senators]

def display_party_affiliation (senators):
    key = {"R": "red", "D" : "blue", "ID": "green"}
    return [key [senator["party"]] for senator in senators]

def display_scatter_plot (response):
    senators = response.json()['results'][0]['members']
    senority_list = calculate_senority(senators)
    votes_with_party = calculate_votes_with_party(senators)
    party_affiliation = display_party_affiliation(senators)
    plt.scatter(votes_with_party, senority_list, c=party_affiliation)
    plt.xlabel("Votes with Party Percentage")
    plt.ylabel("Seniority")
    democrat_blue = mpatches.Patch(color="blue", label="Democrat")
    republican_red = mpatches.Patch(color="red", label="Republican")
    other_green = mpatches.Patch(color="green", label="Other")
    plt.legend(handles=[democrat_blue, republican_red, other_green])
    #plt.show()

#line graph items

def calculate_votes_with_party_average(senators, party):
    filter_senators = [ senator for senator in senators if senator ["party"] ==party]
    return mean(calculate_votes_with_party(filter_senators)) if filter_senators else [0]

congressional_sessions_range = range (101, 118)

senators_by_sessions = [get_congress_session(session).json()['results'][0]['members'] for session in congressional_sessions_range]

republican_mean = [calculate_votes_with_party_average(senators, "R") for senators in senators_by_sessions]
democrat_mean = [calculate_votes_with_party_average(senators, "D") for senators in senators_by_sessions]
independent_mean = [calculate_votes_with_party_average(senators, "ID") for senators in senators_by_sessions]

x = np.arange(len(congressional_sessions_range))
width = 0.25

fig, ax = plt.subplots()
item_1 = ax.bar(x - width, republican_mean, width, label='Republican', color="red")
item_2 = ax.bar(x, democrat_mean, width, label='Democrat', color="blue")
item_3 = ax.bar (x + width, independent_mean, width, label= "Independent", color="green")

plt.xlabel("Party")
plt.ylabel("Average Vote with Party Percentage")

ax.set_xticks(x)
ax.set_xticklabels(congressional_sessions_range)
ax.legend()

fig.tight_layout()

#plt.show()


#demonstrate when Democrats hold majority
congressional_session_117 = get_congress_session(117)
#display_scatter_plot(congressional_session_117)

congressional_session_115 = get_congress_session(115)
#demonstrate when Republicans hold Majority
#display_scatter_plot(congressional_session_115)

get_CSV_data(congressional_session_117)

#Cynical view:  if in minority, consequences for bucking the party are minor 
#Slighty less cynical:  if in minority, legislation that comes to the vote is from the majority party and depending on vote, opposition is preferred in order to appease local constituents 