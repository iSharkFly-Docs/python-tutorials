import time

import stomp

AMQHOST = "nas1120"
AMQPORT = 61616
AMQUSER = "artemis"
AMQPASS = "artemis"
TOPICNAME = "remotingQueue"

hosts = [(AMQHOST, AMQPORT)]
conn = stomp.Connection(host_and_ports=hosts, auto_content_length=False)
conn.connect(username=AMQUSER, passcode=AMQPASS, wait=True)
conn.send(body='Love Python', destination=TOPICNAME)
time.sleep(320)
conn.disconnect()
