# import the installed Jira library
from jira import JIRA
import argparse
import os
import sys
from dotenv import load_dotenv

load_dotenv()

email = os.getenv('EMAIL')
token = os.getenv('TOKEN')
project = os.getenv('PROJECT_KEY')

if not email or not token:
  print('Email and Token must be provided in .env file')
  sys.exit()

if not project:
  print('Project key must be provided in .env file')
  sys.exit()

parser = argparse.ArgumentParser("Assignee")
parser.add_argument("assignee", help="Task assignee name")
args = parser.parse_args()

# Specify a server key. It should be your
# domain name link. yourdomainname.atlassian.net
jiraOptions = {'server': "https://codealpha.atlassian.net/"}


# jira = JIRA(oauth=oauth_dict)
jira = JIRA(
  basic_auth=(email, token),
  options=jiraOptions
)

query = 'project = ' + project + ' AND Assignee = "' + args.assignee + '" AND status IN ("In Progress", "Done")'

# Search all issues mentioned against a project name.
for singleIssue in jira.search_issues(jql_str=query):
	print('=====================================================================\n',
  "No Ticket: ", singleIssue.key,'\n',
  "Description : ", singleIssue.fields.summary,'\n',
	"Status : ", singleIssue.fields.status,'\n',
  "Updated : ", singleIssue.fields.updated,'\n',
  "Labels : ", singleIssue.fields.labels,'\n',
  "Assigneee : ", singleIssue.fields.assignee,'\n',
  "Creator : ", singleIssue.fields.creator,'\n',
  "Priority : ", singleIssue.fields.priority,'\n',
  "Issue Type : ", singleIssue.fields.issuetype,'\n',
  )

