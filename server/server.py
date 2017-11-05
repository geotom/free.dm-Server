'''
The free.dm Server daemon.
@author: Thomas Wanderer
'''

# free.dm Imports
from freedm.daemons.node import NodeDaemon
from freedm.data.objects import DatabaseStore

class ServerDaemon(NodeDaemon):
    '''
    The free.dm Server acts as hub for one or more free.dm Routers.
    It hosts the communication channels and manages access to them.
    '''
    
    _role = 'server'
     
    def onDaemonStart(self):
        # Set up PostgreSQL data store
#         self.data.registerStore(DatabaseStore(**{
#                                                    'name': 'Database',
#                                                    'alias': 'database',
#                                                    'synced': True,
#                                                    'address': self.data.getConfig('daemon.database.address', 'daemon.database.address'),
#                                                    'port': self.data.getConfig('daemon.database.port', 'daemon.database.port'),
#                                                    'user': self.data.getConfig('daemon.database.user', 'daemon.database.user'),
#                                                    'password': self.data.getConfig('daemon.database.password', 'daemon.database.password')
#                                                    }))
        
        #TODO: Remove. Just for testing
        import time
        time.sleep(2)
        
        #TODO: Bring up communications and other background threads
        #TODO: Start RAET communication channels
        #TODO: Start worker threads
        #TODO: Start permanent threads which care for the services (Security, etc.) (Or should a permanent worker thread do this?)
        #TODO: Bind daemon to DBUS to communicate with system services (Or should a permanent worker thread do this?)
        
    def onDaemonHalt(self):
        #TODO: Remove. Just for testing
        import time
        time.sleep(2)
        #TODO: Stop other communication channels
        #TODO: Clean any resource handles
        
    @NodeDaemon.rpcmethod
    def getSystemInfo(self):
        # First get info from super() class
        info = super(self.__class__, self).exposed_getSystemInfo()
        # Add some  temporary data
        clients = [dict(
            section = 1,
            address = '154.587.664.12',
            port = 4651,
            duration = '00:12:01.54654',
            version = 0.3,
            state = 'Running'
            )]
        info['clients'] = clients
        return info
