import producer_server


def run_kafka_server():
	# TODO get the json file path
    input_file = "police-department-calls-for-service.json"

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        bootstrap_servers="localhost:9092",
        client_id=None,
        input_file=input_file,
        topic="police.service.calls",
    )

    if producer.bootstrap_connected():
        print('Connected')

    return producer


def feed():
    producer = run_kafka_server()
    try:
        producer.generate_data()
    except:
        producer.flush()
        producer.close()

    


if __name__ == "__main__":
    feed()
