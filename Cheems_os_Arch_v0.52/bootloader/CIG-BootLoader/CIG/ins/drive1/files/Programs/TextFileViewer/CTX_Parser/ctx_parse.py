import os


d = open("goto_dir.txt", "r")
Lines = d.readlines()
fp = open("file_prs.txt", "r")
filetprs = fp.readlines()
sc = open("show_com.txt", "r")
showc = sc.readlines()

filetps = ""
showcs = ""

os.chdir("..")
os.chdir("..")
os.chdir("CommonFiles")
os.chdir("TextFiles")

f = open(filetps.join(filetprs).replace('\n', ''), "r")
Lines = f.readlines()

# Commands

Start_VAR = "$Text->"
EndFile = "%ENDFILE%"

# Vars

filended = False

def compile_aptfl():
    global Start_VAR, filended
    
    for line in Lines:
        if filended == False:

            cur_line = line.format(1, line.strip())

            if Start_VAR in cur_line:
                cur_commad = cur_line.replace(Start_VAR, "").replace("\n", "")

                if showcs.join(showc).replace('\n', '') == "False":
                    print(cur_commad)

        if filended == False:

            cur_line = line.format(1, line.strip())

            if EndFile in cur_line:
                cur_commad = cur_line.replace(EndFile, "").replace("\n", "")

                filended = True
                if showcs.join(showc).replace('\n', '') == "False":
                    print(cur_commad)
                else:
                    print(Lines)

compile_aptfl()