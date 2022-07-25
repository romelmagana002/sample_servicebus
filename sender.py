from azure.servicebus import ServiceBusClient, ServiceBusMessage
  
CONNECTION_STR = "Endpoint=sb://hncc-dev-se-asia-queue.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=PHqJzxWUbfoI5Yvin+hHGGyIa279VHqWV/V7fcfpPXM="
TOPIC_NAME = "test-topic"
SUBSCRIPTION_NAME = "test-sub"

import sys 
#import datetime

a = str(sys.argv[1])
b = str(sys.argv[2])
#e = datetime.datetime.now()


if(a == 'prod' or a == 'uat'):

    def send_single_message(sender):
    # create a Service Bus message
     message = ServiceBusMessage(a)
    # message = ServiceBusMessage(b)
    # message = ServiceBusMessage(b)
  #  message = ServiceBusMessage(e.strftime ("%Y%m%d"))
    # send the message to the topic
     sender.send_messages(message)
    # sender.send_messages(message1)
    print("Sent a single message")

servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)

with servicebus_client:
    sender = servicebus_client.get_topic_sender(topic_name=TOPIC_NAME)
    with sender:
        send_single_message(sender)


