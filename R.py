import os, sys

if __name__ == "__main__":
   try:
       os.system("git pull")
       __import__("app").menu()
   except Exception as e:
       exit(str(e))