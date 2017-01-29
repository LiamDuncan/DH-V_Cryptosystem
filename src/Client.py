from Node import Node

g = 5
p = 5003

sender = Node( g, p)
receiver = Node( g, p)

ps = sender.getPublic()
pr = receiver.getPublic()

sender.setPartner(pr)
receiver.setPartner(ps)

while(True):
    exchange = sender.getEncryptedMessage()
    receiver.setEncryptedMessage( exchange)
