#!/usr/bin/python3

import requests
import os


rhost = input("Enter the target IP: ")
rport = input("Enter the target port: ")
domain = input("Enter a domain name (press Enter if N/A)")
print("Starting directory fuzzing... ")

path = "wordlists"
filename = "big.txt"
big = os.path.join(path, filename)
with open(big) as file:
    big = file.readlines()

with open(os.path.join("wordlists","big.txt")) as file:
    big = file.readlines() # need to use readlines beacuse read just reads everything as one string

with open(os.path.join("wordlists", "raft-small-words.txt")) as file:
    raft_small_words = file.readlines()

with open(os.path.join("wordlists", "raft-large-files.txt")) as file:
    raft_large_files = file.readlines()

with open(os.path.join("wordlists", "subdomains-top1million-20000.txt")) as file:
    top1million_20000 = file.readlines()

with open(os.path.join("wordlists", "subdomains-top1million-110000.txt")) as file:
    top1million_110000 = file.readlines()

print("Fuzzing using big.txt...")
for directory in big: # This is how you iterate through the file
    directory = directory.rstrip()
    url = f"http://{rhost}:{rport}/{directory}"  # Have to put url into a variable. Cannot put it directly into response variable
    response = requests.get(url, allow_redirects=False) # Make a get request and do not follow any redirects

    if response.status_code == 200:
        print(url)

print("Fuzzing using raft-small-words.txt...")
for directory in raft_small_words:
    directory = directory.rstrip()
    url = f"http://{rhost}:{rport}/{directory}"
    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        print(url)

print("Fuzzing using raft-large-files.txt...")
for directory in raft_large_files:
    directory = directory.rstrip()
    url = f"http://{rhost}:{rport}/{directory}"
    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        print(url)
print("\n", "\n", "\n")

if domain:  # this way we only do subdomain fuzzing if there is a domain to fuzz 
   print("Starting subdomain fuzzing")

   for subdomain in big:
        subdomain = subdomain.rstrip()
        url = f"http://{subdomain}.{domain}:{rport}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(url)
        except (requests.exceptions.ConnectionError, requests.exceptions.InvalidURL):
            pass

   for subdomain in top1million_20000:
        subdomain = subdomain.rstrip()
        url = f"http://{subdomain}.{domain}:{rport}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(url)
        except (requests.exceptions.ConnectionError, requests.exceptions.InvalidURL):
            pass

   for subdomain in top1million_110000:
        subdomain = subdomain.rstrip()
        url = f"http://{subdomain}.{domain}:{rport}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(url)
        except (requests.exceptions.ConnectionError, requests.exceptions.InvalidURL):
            pass
