# KAFKA SASL_SSL with ACL

카프카 SASL_SSL 도커 와 ACL 예제

## Usage

### Run Kafka

1. Create keystore

```sh
export COUNTRY=US
export STATE=IL
export ORGANIZATION_UNIT=SE
export CITY=Chicago
export PASSWORD=secret
bash ./kafka-generate-ssl-automatic.sh
```

create **creds** file for keystore password

```
secret
```

2. Run docker-compose

```yml:docker-compose.yml
docker-compose up -d
```

### Test Acl

```sh
docker exec -it kafka-ssl-1 /bin/bash
```

Command

- create topic

`kafka-topics --zookeeper localhost:22181 --create --topic test --partitions 1 --replication-factor 1`

- create account

`kafka-configs --zookeeper localhost:22181 --alter --add-config 'SCRAM-SHA-256=[iterations=4096,password=test]' --entity-type users --entity-name test`

- delete account

`kafka-configs --zookeeper localhost:22181 --alter --delete-config "SCRAM-SHA-256" --entity-type users --entity-name test`

- access consume

`kafka-acls --authorizer-properties zookeeper.connect=localhost:22181 --add --allow-principal User:test --operation read --topic test`

- access produce

`kafka-acls --authorizer-properties zookeeper.connect=localhost:22181 --add --allow-principal User:test --operation write --topic test`

- access remove

`kafka-acls --authorizer-properties zookeeper.connect=localhost:22181 --remove --allow-principal User:test --operation read --topic test`

### Test python

1. install

`pip install kafka-python`

2. check jks

`keytool -list -keystore kafka.keystore.jks`

3. keysotre.jks to pem

 ```sh:jkstopem.sh
./jkstopem.sh . kafka.keystore.jks secret localhost caroot .
 ```

### Etc command

- pks12 to jks

`keytool -importkeystore -srckeystore kafka.keystore.jks -destkeystore kafka.keystore1.jks -deststoretype jks`