
import asyncio
from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient
from dotenv import load_dotenv
load_dotenv()
import os
import requests


EVENT_HUB_CONNECTION_STR = os.environ["EVENT_HUB_CONNECTION_STR"]
EVENT_HUB_NAME = os.environ["EVENT_HUB_NAME"] 


def get_random_user():
    api_url = "https://randomuser.me/api/?inc=gender,name"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        json_data = response.json()
        return json.dumps(json_data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(
        conn_str=EVENT_HUB_CONNECTION_STR, eventhub_name=EVENT_HUB_NAME
    )
    async with producer:
        # Create a batch.
        #await asyncio.sleep(1)
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        user=get_random_user()
        print(user)
        event_data_batch.add(EventData(user))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)


asyncio.run(run())


