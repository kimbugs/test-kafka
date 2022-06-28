from kafka import KafkaProducer

kafka_brokers='localhost:19093,localhost:29093,localhost:39093'
ca_root_location='CARoot.pem'
cert_location='certificate.pem'
key_location='key.pem'
topic='test'
password='secret'

producer = KafkaProducer(

    bootstrap_servers=kafka_brokers,
    security_protocol='SASL_SSL',
    sasl_mechanism="SCRAM-SHA-256",
    sasl_plain_username='test',
    sasl_plain_password='test',
    #security_protocol='SSL',
    ssl_check_hostname=False,
    ssl_cafile=ca_root_location,
    ssl_certfile=cert_location,
    ssl_keyfile=key_location,
    ssl_password=password
)

producer.send(topic, bytes('Hello Kafka!','utf-8'))
producer.flush()