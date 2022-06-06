from simple_websocket_server import WebSocketServer, WebSocket
from chatbot import get_response
import os
import wikipedia


class ChatServer(WebSocket):

    def handleMessage(self):
        # echo message back to client
        message = self.data
        
               
               
        if message ==  "ನೋಟ್ ಪ್ಯಾಡ್ ಅನ್ನು ತೆರೆ" :
           os.startfile('C:/WINDOWS/system32/notepad.exe')
           
          
        if message ==  "ಪವರ್ಪಾಯಿಂಟ್ ಅನ್ನು ತೆರೆ" :
          os.startfile('C:/Program Files/Microsoft Office/Office16/POWERPNT.exe')
        if message ==  "ಬ್ರೌಸರ್ ಅನ್ನು ತೆರೆ" :
          os.startfile('C:/Program Files/Mozilla Firefox/firefox.exe')
        if message ==  "ಎಕ್ಲಿಪ್ಸ್ ಅನ್ನು ತೆರೆ" :
          os.startfile('C:/Users/Sagar/eclipse/jee-photon/eclipse/eclipse.exe')
          response = get_response(message)
          self.sendMessage(response)
        
          
        else:
         #wikipedia.set_lang("kn")
         #self.sendMessage(wikipedia.summary(message,senetences=2))
         response = get_response(message)
         self.sendMessage(response)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')



server = WebSocketServer('', 8000, ChatServer)
server.serveforever()
