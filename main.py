from replit import clear
from art import *
bidslist=[]
#HINT: You can call clear() to clear the output in the console.
def display_logo():
  print(logo)

def enlistthem(n, b):
  bidslist.append({n: b})
def decidewinningbid():
  currmaxname = ''
  currmaxbid = 0
  # print(currmax)
  for record in bidslist:
    print(record)
    for key in record:
      # print(key)
      if record[key] > currmaxbid:
        currmaxname = key
        currmaxbid = record[key]

  currmax = {currmaxname: currmaxbid}
  return(currmax)


clear()
display_logo()
bidslist=[{"ila": 71}, {"amy": 22}, {"gru": 33}, {"pay": 44}]
moreusersflag = True
# while moreusersflag:
#   name = input("Enter your name: ")
#   bid = int(input("Enter your bid amound: "))
#   enlistthem(name, bid)
#   moreusers = input("Are there more bidders? Say 'yes' or 'no': ")
#   if moreusers == 'yes':
#     clear()
#     moreusersflag = True
#   else:
#     moreusersflag = False
winner = {}
winner = decidewinningbid()    
print(winner)