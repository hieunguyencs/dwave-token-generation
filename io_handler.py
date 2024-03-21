import datetime
import os


def write_history(dwave_token):
    with open("output/history.txt", 'a') as f:
        f.write(dwave_token + '\n')
        f.write("\tCreated on: " + str(datetime.datetime.utcnow()) + " (UTC)" + '\n')


def write_tokens(token):
    # num_cur_tokens = len(os.listdir("token"))
    # with open(f"token/{num_cur_tokens + 1}.txt", 'w') as f:
    #     f.write(token + '\n')
    with open("output/all_tokens.txt", 'a') as f:
        f.write(token + '\n')


