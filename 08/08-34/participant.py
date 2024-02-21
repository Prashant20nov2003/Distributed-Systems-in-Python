import channel, stablelog, random #-
from const2PC import * #-
#-
class Participant:
  def __init__(self, chanID, coordID, partID, partIDSet): #-
    self.chan        = channel.Channel(chanID) #-
    self.partID      = partID #-
    self.chan.join(partID)    #-
#-
    self.coordinator  = coordID   #-
    self.participants = partIDSet #-
    self.participants.remove(self.partID) #-
#-    
    self.log         = stablelog.createLog(self.partID) #-
#-
  def do_work(self): #-
    if random.randint(0,99) < 50: #-
      return LOCAL_ABORT #-
    else: #-
      return LOCAL_SUCCESS #-
#-
  def run(self):
    self.log.info('INIT') 
#-
    msg = self.chan.recvFrom(self.coordinator, BLOCK, TIMEOUT) 
    if msg == -1:  # Crashed coordinator - give up entirely
      decision = LOCAL_ABORT
    else: # Coordinator will have sent VOTE_REQUEST
      decision = self.do_work() 
      if decision == LOCAL_ABORT:
        self.chan.sendTo(self.coordinator, VOTE_ABORT)
        self.log.info('LOCAL_ABORT')
#-
      else: # Ready to commit, enter READY state
        self.log.info('READY') 
        self.chan.sendTo(self.coordinator, VOTE_COMMIT)
#-
        msg = self.chan.recvFrom(self.coordinator, BLOCK, TIMEOUT)
        self.log.info(msg) #-
        if msg == -1: # Crashed coordinator - check the others
          self.log.info('NEED_DECISION')
          self.chan.sendTo(self.participants, NEED_DECISION)
          while True:
            msg = self.chan.recvFromAny()
            if msg[1] in [GLOBAL_COMMIT, GLOBAL_ABORT, LOCAL_ABORT]:
              decision = msg[1]
              break
#-
        else: # Coordinator came to a decision
          decision = msg[1]
#-
    if decision == GLOBAL_COMMIT: 
      self.log.info('COMMIT')
    else: # decision in [GLOBAL_ABORT, LOCAL_ABORT]:
      self.log.info('ABORT')
#-
    while True: # Help any other participant when coordinator crashed
      msg = self.chan.recvFrom(self.participants)
      if msg[1] == NEED_DECISION:
        self.chan.sendTo([msg[0]], decision)
