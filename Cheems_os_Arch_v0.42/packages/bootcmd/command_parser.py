with open('command_sent.txt', 'r') as cmd:
    cmds = cmd.read().replace(' ', '')

fp = open('cur_cmd_sent.txt', 'w')
fp.write(cmds)
fp.close()

quit()