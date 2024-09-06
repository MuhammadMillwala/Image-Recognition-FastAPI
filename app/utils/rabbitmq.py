import pika

def connect_to_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='image_queue')
    return channel

def callback(ch, method, properties, body):
    print(f"Received {body}")
    # Add your image processing logic here
    # process_image(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

def consume_images():
    channel = connect_to_rabbitmq()
    channel.basic_consume(queue='image_queue', on_message_callback=callback)
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
