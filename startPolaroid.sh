#! /bin/sh

### BEGIN INIT INFO
# Provides:          Polaroid
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6   
### END INIT INFO


# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting polaroid.py"
    python /usr/local/bin/polaroid.py &
    ;;
  stop)
    echo "Stopping polaroid.py"
    pkill -f /usr/local/bin/polaroid.py
    ;;
  *)
    echo "Usage: /etc/init.d/polaroid.py {start|stop}"
    exit 1
    ;;
esac

exit 0