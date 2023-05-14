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

========================================================================================
<h3>Thursday 27-April Project Brief: Visualizing streaming data with Streamlit </h3>

![streamlit](https://cdn.analyticsvidhya.com/wp-content/uploads/2021/06/39595st.jpeg)

<h4>Introduction</h4>

<p>In this project, you will create a real-time data visualization dashboard using Streamlit to analyze
streaming data from Reddit to identify fraud in telecommunications. The project will involve
connecting to Reddit's API, collecting real-time posts, processing the posts to extract useful
information, and visualizing the data using Streamlit.</p>

<h4>Problem Statement</h4>
<p>Fraud in telecommunications is a significant problem that costs the industry billions of dollars
annually. Fraudsters use various techniques to exploit telecom infrastructure weaknesses,
including hacking into phone systems, stealing identities, and exploiting vulnerabilities in billing
systems. The challenge for telecom companies is to detect and prevent fraud in real-time before
it causes significant financial damage.</p>

<p>Your task is to develop a real-time data visualization dashboard that monitors Reddit for
mentions of telecoms fraud and other related keywords, such as "telecoms scam", "phone
fraud", "billing fraud", and "identity theft". You will extract useful information from the posts, such
as the post text, user name, subreddit, and date/time, and use this information to analyze the
data for patterns and trends related to telecom fraud.</p>

<h4>Project Requirements</h4>
● Connect to Reddit's API and collect real-time posts related to telecom fraud and other
related keywords.<br>
● Process the posts to extract useful information, including the post text, user name,
subreddit, and date/time.<br>
● Analyze the data to identify patterns and trends related to telecom fraud and other
related keywords.<br>
● Use Streamlit to create an interactive data visualization dashboard that displays
real-time information about telecom fraud and other related keywords.<br>
● The dashboard should include at least one chart or graph that displays the data
meaningfully, e.g., a bar chart showing the number of fraud mentions by subreddit or a
line chart showing the frequency of fraud mentions over time.<br>
● The dashboard should be easy to use and visually appealing, with clear and concise
labels and instructions<br>

<h4>Deliverables</h4>
● Python script to collect and process real-time posts from Reddit API.<br>
● Interactive data visualization dashboard created using Streamlit.<br>
● Deployment of the dashboard to a cloud-based platform.<br>

<h4><i>Steps to access the dashboard</i></h4>
The application code is in file - <b>streamlit_app.py</b><br>
The libraries that need to be imported to run the dashboard are in file - <b>requirements.txt</b><br>
The dashboard is accessible at URL - <b>https://joekibz-moringa-wk9-streamlit-app-sywmbo.streamlit.app/</b>


