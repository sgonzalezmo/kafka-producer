import typer

app = typer.Typer()
import json

from kafka import KafkaProducer


def _send_operation(
    kafka_server: str,
    kafka_port: int,
    kafka_topic: str,
    operation: str,
    a: int,
    b: int,
):
    # Connection to Kafka
    producer = KafkaProducer(
        bootstrap_servers=f"{kafka_server}:{kafka_port}",
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    # Send message
    producer.send(kafka_topic, {"operation": operation, "a": a, "b": b})


@app.command()
def add(kafka_server: str, kafka_port: int, kafka_topic: str, a: int, b: int):
    _send_operation(kafka_server, kafka_port, kafka_topic, "add", a, b)


@app.command()
def subtract(
    kafka_server: str, kafka_port: int, kafka_topic: str, a: int, b: int
):
    _send_operation(kafka_server, kafka_port, kafka_topic, "subtract", a, b)


@app.command()
def multiply(
    kafka_server: str, kafka_port: int, kafka_topic: str, a: int, b: int
):
    _send_operation(kafka_server, kafka_port, kafka_topic, "multiply", a, b)


@app.command()
def divide(
    kafka_server: str, kafka_port: int, kafka_topic: str, a: int, b: int
):
    _send_operation(kafka_server, kafka_port, kafka_topic, "divide", a, b)
