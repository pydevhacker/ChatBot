from slackclient import SlackClient

def get_bot_id_from_cache(bot_name):
    try:
        with open('bot_names', 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip().split(':')
                if line[0] == bot_name:
                    return line[1]
    except:
        print('No File')
    return None

def store_bot_id_in_cache(bot_name, bot_id):
    with open('bot_names', 'a') as file:
        file.write(bot_name + ':' + bot_id)

def get_bot_id(bot_name, bot_token):

    slack_client = SlackClient(bot_token)

    cache = get_bot_id_from_cache(bot_name)
    if cache is not None:
        return cache, slack_client

    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == bot_name:
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
                store_bot_id_in_cache(bot_name, user.get('id'))
                return user.get('id'), slack_client
    else:
        print("could not find bot user with the name " + bot_name)
    return None, None
