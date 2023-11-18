from telethon.tl.functions.channels import InviteToChannelRequest


def inviting(client, channel, users):
    client(InviteToChannelRequest(
        channel=channel,
        users=[users]
    ))


def parsing(client, index):
    all_participants = []
    all_participants = client.get_participants(index)
    with open('participants.txt', 'r+') as f:
        for user in all_participants:
            if user.username:
                if ('Bot' not in user.username) and ('bot' not in user.username):
                    if (('@' + user.username + '\n') not in f.read()):
                        f.write('@' + user.username + '\n')
                    else:
                        continue
                else:
                    continue
            else:
                continue