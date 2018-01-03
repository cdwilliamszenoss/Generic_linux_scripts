
if evt.severity == 5 and 'absolute value of offset' in evt.summary:
#  evt._action = 'history'
#  Use eventState to suppress the event to the console. To show suppressed events, select "Suppressed" on Status button
   evt.eventState = 2

# Use to Drop events
#  if evt.message.find("twisted.internet.error") >= 0:
#  evt._action = "drop"


