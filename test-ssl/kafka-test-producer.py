import ssl
from kafka import KafkaConsumer, KafkaProducer

kafka_brokers='localhost:19093,localhost:29093,localhost:39093'
ca_root_location='CARoot.pem'
cert_location='certificate.pem'
key_location='key.pem'
topic='test'
password='secret'

# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
# context.load_verify_locations('snakeoil-ca-1.crt')

producer = KafkaProducer(

    bootstrap_servers=kafka_brokers,
    # ssl_context=context,
    security_protocol='SASL_SSL',
    sasl_mechanism="SCRAM-SHA-256",
    sasl_plain_username='test',
    sasl_plain_password='test',
    ssl_check_hostname=False,
    ssl_cafile=ca_root_location,
    ssl_certfile=cert_location,
    ssl_keyfile=key_location,
    ssl_password=password
)

producer.send(topic, bytes('Hello Kafka!','utf-8'))
producer.flush()