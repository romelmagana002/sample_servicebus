from azure.servicebus import ServiceBusClient, ServiceBusMessage
  
CONNECTION_STR = "Endpoint=sb://hncc-dev-se-asia-queue.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=PHqJzxWUbfoI5Yvin+hHGGyIa279VHqWV/V7fcfpPXM="
TOPIC_NAME = "test-topic"
SUBSCRIPTION_NAME = "test-sub"

servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)

with servicebus_client:
    # get the Subscription Receiver object for the subscription
    receiver = servicebus_client.get_subscription_receiver(topic_name=TOPIC_NAME, subscription_name=SUBSCRIPTION_NAME, max_wait_time=5)
    with receiver:
        for msg in receiver:
            print("Received: Job done on " + str(msg))
            # complete the message so that the message is removed from the subscription
            receiver.complete_message(msg)
