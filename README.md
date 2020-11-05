# ALMABASE ASSIGNMENT

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

In This assignment I had to find the n most popular repositories of a given organization on Github (Eg:https://github.com/google) based on the number of forks. For each such repo I had to find the top m committees and their commit counts.

# CODE LOGIC

I used  github's API to retrieve the all the repositories of a particular organisation and then extracted the top N repositories based on fork count(descending order). For the extraction of top N repositories I used an inbuilt HEAP data Structure to efficiently extract such repos in the least possible time complexity.

Then For each repository I retrieved all the contributors / committees and again extracted top M contributors based on the no. of commits(descending order). Again I used HEAP data structure for optimal extraction in reduced time complexity.

### PREQUISITES(To run app locally)

* Python 3.8 and pip should be installed.
* requests library (install using "pip install requests")

### HOW TO RUN
* Create an environment on your desktop with the above mentioned prerequisites.
* Clone my repository
* Create a Personal Access Token (PAT) on github using this link : https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token
* Copy this token and open the 'config.py' file and replace 'YOUR_TOKEN_ID' with the generated token id as a string enclosed in '' without any extra spaces.
* in the Command Line write 
```sh
python almabaseProject.py
```
* now intract with the program suitably based on the prompts

### REASON TO GENERATE PAT
github allows on 60 unauthorised API calls in 1 hour which is very less for this program's purpose. To make authenticated calls we need to genrate Personal access tokens to increase the limit to 5000.

### SCREENSHOTS
![query output](https://github.com/nikhilgogia/AlmabaseProject/blob/master/Images/queryOutput.png)