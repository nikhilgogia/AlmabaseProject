import heapq
import requests
from config import config

tokenId = config['TOKEN_ID']
apiPrefix = 'https://api.github.com/'
queryString = '?access_token='+tokenId+'&per_page=100&page='

#Collection of input from user
orgName = input("Enter organisation's name: ")
N = int(input("Enter N(number of top repositories to display): "))
M = int(input("Enter M(number of top committees to display for each repository): "))
print()

#retrieving all the repositories for the received organisation
repoList=[]
topNRepoDict = {}
topMCommitteesDict = {}
pageNum=1
while(True):     #The result can consist of multiple pages, we loop until we reach the last page of our search
    request = requests.get(apiPrefix+'users/'+orgName+'/repos'+queryString+str(pageNum))
    json = request.json()
    if(len(json) == 0):        #if there is no repo in json, it means that we have iterated over all the repos
        break
    for repo in range(len(json)):
        repoList.append((-json[repo]["forks"],json[repo]["name"]))   #storing no. of forks and repo name in repoList as tuples
    pageNum+=1

heapq.heapify(repoList)   #creating a heap of the repoList
repoCount = 0
while(repoCount<N and len(repoList)>0):     #popping top N repos from the heap
    forkCount,repoName = heapq.heappop(repoList)
    topNRepoDict[repoName] = -forkCount     #storing repoName as key and fork count as value in dictionary
    topMCommitteesDict[repoName] = []       #storing repoName as key and empty list as value in 2nd dictionary
    repoCount+=1

#for each repo we will be retrieving all its committees and finding top M of them
for repo in topMCommitteesDict:
    committeesList = [] #to store committees for each repo
    pageNum = 1
    while(True):  #to iterate over all pages of search result
        request = requests.get(apiPrefix+'repos/'+orgName+'/'+repo+'/contributors'+queryString+str(pageNum))
        json = request.json()
        if(len(json) == 0):
            break
        for contributor in range(len(json)):
            committeesList.append((-json[contributor]["contributions"],json[contributor]["login"])) #storing no. of commits and contributor name as tuple
        pageNum+=1

    heapq.heapify(committeesList) #converting comitteesList to a heap
    contributorCount = 0
    while(contributorCount<M and len(committeesList)>0): #extracting top M contributors from the heap
        contributionCount,contributorName=heapq.heappop(committeesList)
        topMCommitteesDict[repo].append([contributorName,-contributionCount]) #storing tuple in the list for that particular repo
        contributorCount+=1

#displaying result Data
for repo in topNRepoDict:
    print ("Repository name:", repo)
    print ("No. of forks:", topNRepoDict[repo])
    print ("Top committees for the repository are as follows:- ")
    print ()
    for contributor in topMCommitteesDict[repo]:
        print ("Contributor name:", contributor[0])
        print ("No. of commits made by the Contributor:", contributor[1])
        print ()
