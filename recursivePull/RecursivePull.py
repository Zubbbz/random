import os

Dir = os.getcwd()

def PullSubs(Dir):
    for subdir in os.listdir(Dir):
        fullpath = os.path.abspath(os.path.join(Dir, subdir))
        if os.path.isfile(fullpath): continue
        os.chdir(fullpath)
        os.system("git pull")

PullSubs(Dir)