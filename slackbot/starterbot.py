import time
from slackclient import SlackClient

BOT_NAME = 'starterbot'
BOT_ID = 'U5BGB985D'

slack_client = SlackClient('xoxb-181555314183-F4QgugVSWSoG74WQZryPbTht')

#constants
AT_BOT = "<@" + BOT_ID + ">"
START_CMD = "!"

def handle_command(command, channel):
    #response = process_command(command)
    response = "Sure ... write some more code then I can do that!"
    slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)

def process_command(command):
    q = ''
    a = ''
    if command.startwith('q:'):
        q = command[2:]
    if command.startwith('a:'):
        a = command[2:]


def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            print(output)
            if output and 'text' in output and AT_BOT in output['text']:
                return output['text'].split(AT_BOT)[1].strip().lower(), output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1
    if slack_client.rtm_connect():
        print('StarterBot Connected and running!')
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print('Connection failed. Invalid Slack token or bot ID?')