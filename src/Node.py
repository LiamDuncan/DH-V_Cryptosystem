import random
import nodeIO

class Node:

    def __init__( self, g, p):
        self.g = g
        self.p = p
        self.privateKey = random.randrange(100)
        self.publicKey = (g^self.privateKey)%p

    def getEncryptedMessage( self):
        #message = input( "Type a message... \nSender: ")
        message = input( "Type a message... \n")
        em = self.encrypt( message)
        return em

    def setEncryptedMessage( self, em):
        message = self.decrypt(em)
        #print("Receiver: " + message)
        nodeIO.window( message)
    
    def getPublic( self):
        return self.publicKey

    def setPartner( self, pk):
        self.key = (pk^self.privateKey)%self.p

    def encrypt( self, message):
        encryptedMessage = ""
        for character in message:
            encryptedChar = chr(self.vigenere(ord(character)))
            encryptedMessage += encryptedChar
        return encryptedMessage
        
    def decrypt( self, encryptedMessage):
        message = ""
        for character in encryptedMessage:
            char = chr(self.unvigenere(ord(character)))
            message += char
        return message

    def vigenere( self, charNumber):
        return (charNumber + self.key)%127

    def unvigenere( self, charNumber):
        return (charNumber - self.key)%127
        
