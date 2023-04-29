# Moringa-wk9 : Apache Kafka and Streamlit exploration

<h3>Wednesday 26-April Project Brief: Data Streaming with Kafka</h3>

![apache kafka](https://user-images.githubusercontent.com/107838961/235288674-ce2139fd-f8dd-44c2-aab8-0531a69c48bf.png)

<h4 align="center">Background: Telecommunications Mobile Money Data Engineering with
Kafka</h4>

<p>In this project, you will work with telecommunications mobile money data to build a Kafka data
engineering solution. You will be provided with a dummy json file containing sample data that
you will use to test your solution.</p>

<p>The project aims to build a Kafka pipeline that can receive real-time data from
telecommunications mobile money transactions and process it for analysis. The pipeline should
be designed to handle high volumes of data and ensure that the data is processed efficiently.</p>

<p>To complete this project, you will need to follow these steps:
<br>1. <b>Set up a Kafka cluster:</b> You must set up a Kafka cluster that can handle high volumes
of data. You can use either a cloud-based or on-premises Kafka cluster.
<br>2. <b>Develop a Kafka producer:</b> You must develop a Kafka producer that can ingest data
from telecommunications mobile money transactions and send it to the Kafka cluster.
The producer should be designed to handle high volumes of data and ensure that the
data is sent to the Kafka cluster efficiently.
<br>3. <b>Develop a Kafka consumer:</b> You must develop a Kafka consumer to receive data from
the Kafka cluster and process it for analysis. The consumer should be designed to
handle high volumes of data and ensure that the data is processed efficiently.
<br>4. <b>Process the data:</b> Once you have set up the Kafka pipeline, you must process the data
for analysis. This may involve cleaning and aggregating the data, performing
calculations, and creating visualizations.
<br>5. <b>Test the solution:</b> You must test your solution using the provided dummy json file. The
file contains sample data that you can use to ensure that your Kafka pipeline is working
correctly.</p>

<p>Here’s the dummy JSON file that represents our mobile money data.<br>
{<br>
"transaction_id": "12345",<br>
"sender_phone_number": "256777123456",<br>
"receiver_phone_number": "256772987654",<br>
"transaction_amount": 100000,<br>
"transaction_time": "2023-04-19 12:00:00"<br>
}</p>

<b><i>Steps to setup the pipeline</b></i>

1- Goto https://confluent.cloud/ and setup a kafka cluster and topic<br>
2- Get the connection details for your cluster instance<br>
3- In the attached .py file find the code section with below entries. Update the below connection details to reflect the connection details generated for your own confluence cluster instance.<br>

<i>bootstrap_servers = '#YOUR_URL#.confluent.cloud:9092'
<br>security_protocol = 'SASL_SSL'
<br>sasl_mechanism = 'PLAIN'
<br>sasl_plain_username = '#YOUR_USERNAME#'
<br>sasl_plain_password = '#YOUR_PASSWORD#'
<br>topic = 'my_pipeline'</i>

4- Run the .py file to start the streaming pipeline
