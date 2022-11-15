import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")
client = WebClient(token=BOT_TOKEN)


def get_users():
    # access google sheet of roster, which should have name, email, and weights
    # get the emails of people by parsing csv or however
    emails = {"omaryu@berkeley.edu": 3}
    
    # tag by ID so get IDs
    # users = {client.users_lookupByEmail(email=address): emails[address] for address in emails}
    # ids = [user["user"]["id"] for user in users]
    ids = {}
    for address in emails:
        user = client.users_lookupByEmail(email=address)
        id = user["user"]["id"]
        weight = emails[address]
        ids[id] = weight
    
    # dummy info 
    ids['UT3A3434'] = 3
    ids['U535gT4'] = 3

    # return mapping of user id : weight
    return ids


def get_posts():
    # get ed post links
    # parse out discussion number for better message formatting
    unparsed = ["https://edstem.org/us/courses/25379/discussion/1983557",
             "https://edstem.org/us/courses/25379/discussion/2011307",
             "https://edstem.org/us/courses/25379/discussion/1741197",
            ]

    posts = {}
    for link in unparsed:
        index = link.index("n/") + 2
        disc_num = link[index:]
        posts[disc_num] = link

    # return mapping of disc num : link
    return posts


def assign(users, posts):
    # should ideally return a mapping of users to posts
    # do some weighting stuffs
    # just as an example since im the only one in the test slack
    assignments = {}

    for user, post in zip(users, posts):          # assuming that users and post have same length, which definitely won't be true
        post_info = [post, posts[post]]
        assignments[user] = post_info
    
    return assignments


ids = get_users()
posts = get_posts()
assignments = assign(ids, posts)

try:
    message = ""

    prefix = ("Good morning! Here are today's Ed assignments. "
               "You will receive a daily reminder about your unresolved Ed posts. "
               "*If you do not know how to answer your post(s), post in #ed.* \n\n"
             )

    message += prefix

    for mapping in assignments:
        info = f'<@{mapping}> please help <{assignments[mapping][1]}|@{assignments[mapping][0]}> \n'
        message += info

    response = client.chat_postMessage(channel="general", text=message)

except SlackApiError as e:
    assert e.response["error"]