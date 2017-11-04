#!/usr/bin/env ../vpython3.6/bin/python3
#!/usr/bin/env python3

# Imports
import os, sys

# Check import path (for development env)
if not os.path.exists('freedm'):
    sys.path.append(os.path.realpath(__file__).replace(os.path.basename(__file__), '../free.dm-Common'))

# Run the daemon    
if __name__ == '__main__':
    from freedm.daemons.server import ServerDaemon
    s = ServerDaemon()