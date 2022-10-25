import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")
client = WebClient(token=BOT_TOKEN)

# users = {'ok': True, 'members': [
#     {'id': 'USLACKBOT', 'team_id': 'T04828CPLRH', 'name': 'slackbot', 'deleted': False, 'color': '757575', 'real_name': 'Slackbot', 'tz': 'America/Los_Angeles', 'tz_label': 'Pacific Daylight Time', 'tz_offset': -25200, 
#     'profile': {'title': '', 'phone': '', 'skype': '', 'real_name': 'Slackbot', 'real_name_normalized': 'Slackbot', 'display_name': 'Slackbot', 'display_name_normalized': 'Slackbot', 'fields': {}, 'status_text': '', 'status_emoji': '', 'status_emoji_display_info': [], 'status_expiration': 0, 'avatar_hash': 'sv41d8cd98f0', 'always_active': True, 'first_name': 'slackbot', 'last_name': '', 'image_24': 'https://a.slack-edge.com/80588/img/slackbot_24.png', 'image_32': 'https://a.slack-edge.com/80588/img/slackbot_32.png', 'image_48': 'https://a.slack-edge.com/80588/img/slackbot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/slackbot_72.png', 'image_192': 'https://a.slack-edge.com/80588/marketing/img/avatars/slackbot/avatar-slackbot.png', 'image_512': 'https://a.slack-edge.com/80588/img/slackbot_512.png', 'status_text_canonical': '', 'team': 'T04828CPLRH'}
#     , 'is_admin': False, 'is_owner': False, 'is_primary_owner': False, 'is_restricted': False, 'is_ultra_restricted': False, 'is_bot': False, 'is_app_user': False, 'updated': 0, 'is_email_confirmed': False, 'who_can_share_contact_card': 'EVERYONE'}
#     , {'id': 'U048F048TDF', 'team_id': 'T04828CPLRH', 'name': 'omaryu', 'deleted': False, 'color': '9f69e7', 'real_name': 'omaryu', 'tz': 'America/Los_Angeles', 'tz_label': 'Pacific Daylight Time', 'tz_offset': -25200, 'profile': {'title': '', 'phone': '', 'skype': '', 'real_name': 'omaryu', 'real_name_normalized': 'omaryu', 'display_name': '', 'display_name_normalized': '', 'fields': None, 'status_text': '', 'status_emoji': '', 'status_emoji_display_info': [], 'status_expiration': 0, 'avatar_hash': 'g96b5d41cd10', 'email': 'omaryu@berkeley.edu', 'first_name': 'omaryu', 'last_name': '', 'image_24': 'https://secure.gravatar.com/avatar/96b5d41cd10b2a76cb5f595413bc412b.jpg?s=24&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0000-24.png', 'image_32': 'https://secure.gravatar.com/avatar/96b5d41cd10b2a76cb5f595413bc412b.jpg?s=32&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0000-32.png', 'image_48': 'https://secure.gravatar.com/avatar/96b5d41cd10b2a76cb5f595413bc412b.jpg?s=48&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0000-48.png', 'image_72': 'https://secure.gravatar.com/avatar/96b5d41cd10b2a76cb5f595413bc412b.jpg?s=72&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0000-72.png', 'image_192': 'https://secure.gravatar.com/avatar/96b5d41cd10b2a76cb5f595413bc412b.jpg?s=192&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0000-192.png', 'image_512': 'https://secure.gravatar.com/avatar/96b5d41cd10b2a76cb5f595413bc412b.jpg?s=512&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0000-512.png', 'status_text_canonical': '', 'team': 'T04828CPLRH'}, 'is_admin': True, 'is_owner': True, 'is_primary_owner': True, 'is_restricted': False, 'is_ultra_restricted': False, 'is_bot': False, 'is_app_user': False, 'updated': 1666728303, 'is_email_confirmed': True, 'who_can_share_contact_card': 'EVERYONE'}, {'id': 'U048S36HUKA', 'team_id': 'T04828CPLRH', 'name': 'ed_bot', 'deleted': False, 'color': '4bbe2e', 'real_name': 'Ed Bot', 'tz': 'America/Los_Angeles', 'tz_label': 'Pacific Daylight Time', 'tz_offset': -25200, 'profile': {'title': '', 'phone': '', 'skype': '', 'real_name': 'Ed Bot', 'real_name_normalized': 'Ed Bot', 'display_name': '', 'display_name_normalized': '', 'fields': None, 'status_text': '', 'status_emoji': '', 'status_emoji_display_info': [], 'status_expiration': 0, 'avatar_hash': 'gbd753dbf917', 'api_app_id': 'A047VNJCER4', 'always_active': False, 'bot_id': 'B0484RHAS12', 'first_name': 'Ed', 'last_name': 'Bot', 'image_24': 'https://secure.gravatar.com/avatar/bd753dbf917675b920f99c283ed669da.jpg?s=24&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0020-24.png', 'image_32': 'https://secure.gravatar.com/avatar/bd753dbf917675b920f99c283ed669da.jpg?s=32&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0020-32.png', 'image_48': 'https://secure.gravatar.com/avatar/bd753dbf917675b920f99c283ed669da.jpg?s=48&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0020-48.png', 'image_72': 'https://secure.gravatar.com/avatar/bd753dbf917675b920f99c283ed669da.jpg?s=72&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0020-72.png', 'image_192': 'https://secure.gravatar.com/avatar/bd753dbf917675b920f99c283ed669da.jpg?s=192&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0020-192.png', 'image_512': 'https://secure.gravatar.com/avatar/bd753dbf917675b920f99c283ed669da.jpg?s=512&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0020-512.png', 'status_text_canonical': '', 'team': 'T04828CPLRH'}, 'is_admin': False, 'is_owner': False, 'is_primary_owner': False, 'is_restricted': False, 'is_ultra_restricted': False, 'is_bot': True, 'is_app_user': False, 'updated': 1666728833, 'is_email_confirmed': False, 'who_can_share_contact_card': 'EVERYONE'}], 'cache_ts': 1666731347, 'response_metadata': {'next_cursor': ''}}


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
# print(ids)
# print(posts)

assignments = assign(ids, posts)

# print(assignments)

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

    # message = ("Good morning! Here are today's Ed assignments. "
    #            "You will receive a daily reminder about your unresolved Ed posts. "
    #            "*If you do not know how to answer your post(s), post in #ed*. \n\n"
    #            "<@U048F048TDF> please help <https://edstem.org/us/courses/25379/discussion/1983557|@1983557>" 
    #           )


    response = client.chat_postMessage(channel="general", text=message)

except SlackApiError as e:
    assert e.response["error"]