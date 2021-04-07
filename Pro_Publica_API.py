import requests, json, matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from statistics import mean

#API key for ProPublica is in pro_publica_api.txt and is not uploaded to Git
with open("pro_publica_api.txt") as f:
    pro_publica_key = f.read()

#Sessions of Congress with necessary voting percentage data start at session 101 year 1989 to 1991  and end at current, session 117

pro_publica_req = 'https://api.propublica.org/congress/v1/{}/senate/members.json'

def get_congress_session(number):
    return requests.get(pro_publica_req.format(number), headers = {"X-API-Key" : pro_publica_key})

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
    plt.show()

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

ax.set_xticks(x)
ax.set_xticklabels(congressional_sessions_range)
ax.legend()

fig.tight_layout()

plt.show()


display_scatter_plot(get_congress_session(117))

