from slackbot import bot
from slackbot import calculator
import time

BOT_NAME = 'starterbot'
BOT_TOKEN = 'xoxb-181555314183-F4QgugVSWSoG74WQZryPbTht'

id, client = bot.get_bot_id(BOT_NAME, BOT_TOKEN)

AT_BOT = "<@" + id + ">"
EXAMPLE_COMMAND = "do"

def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            print('output', output)
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None

def handle_command(command, channel):
    response = 'Start command with "do"!!'
    if command.startswith(EXAMPLE_COMMAND):
        response = calculator.calculate(command)
    print('response', response)
    client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)

def connect(slack_client):
    READ_WEBSOCKET_DELAY = 1
    if client.rtm_connect():
        print('StarterBot Connected and running!')
        while True:
            command, channel = parse_slack_output(client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print('Connection failed. Invalid Slack token or bot ID?')

connect(client)