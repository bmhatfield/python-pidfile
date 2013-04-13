python-pidfile
==============

A Pidfile Context Manager compatible with python-daemon's DaemonContext()


Thanks
======

This is a direct copy (minus example usage in file) from an ActiveState recipe found here:
http://code.activestate.com/recipes/577911-context-manager-for-a-daemon-pid-file/

Example Usage
=============
```python
import daemon
context = daemon.DaemonContext()
context.pidfile = PidFile("/var/run/mydaemon")
```

or

```python
with daemon.DaemonContext(working_directory=".", pidfile=PidFile(pidpath)):
  #do your daemonstuff here
```
