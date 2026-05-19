☁️ Serverless CSV Processing Pipeline using AWS (S3 + Lambda + DynamoDB + SNS)
📌 Project Overview

This project was developed as part of a Cloud Computing & Data Engineering learning track.

The objective of this project is to design and implement a fully serverless data processing pipeline using AWS services that automatically processes CSV files uploaded to an S3 bucket, stores structured data into DynamoDB, and sends real-time email notifications using SNS.

The solution focuses on:

Automating data ingestion using event-driven architecture
Processing structured CSV data using AWS Lambda
Storing processed data in DynamoDB
Enabling real-time notifications using SNS
Deploying infrastructure using CloudFormation (Infrastructure as Code)
🎯 Project Goal

The primary goal of this project is to eliminate manual data processing and build a scalable, automated cloud-based pipeline for handling structured CSV data.

The system provides:

Automated file processing
Real-time data storage
Notification-based monitoring
Scalable serverless architecture
Infrastructure automation using IaC
🚩 Business Problem

Organizations often face challenges such as:

Manual processing of uploaded files
Delayed data availability for analysis
Lack of automated notifications on data ingestion
Inefficient and error-prone data entry workflows
Difficulty in scaling traditional ETL systems

This project addresses these challenges by implementing a fully automated AWS-based pipeline.

👨‍💻 My Role
Cloud Developer – Serverless Data Pipeline Implementation
Responsibilities:
Designed and implemented AWS serverless architecture
Developed Lambda function for CSV processing
Configured S3 event-driven triggers
Designed DynamoDB schema for structured storage
Integrated SNS for email notifications
Built CloudFormation template for infrastructure automation
Configured IAM roles and permissions
🏗️ Solution Architecture
🔹 AWS Components
Amazon S3 → File storage & event trigger
AWS Lambda → CSV processing engine
Amazon DynamoDB → Data storage layer
Amazon SNS → Notification system
AWS IAM → Security & access control
AWS CloudFormation → Infrastructure as Code
📊 Dataset
studentId,name,department,marks
101,John,IT,85
102,Alice,CSE,91
103,Bob,ECE,78
🗄️ DynamoDB Schema
Field	Type	Key Type
studentId	String	Partition Key
name	String	-
department	String	-
marks	Number	-
🔔 Notification System (SNS)

After successful processing of the CSV file:

Lambda publishes a message to SNS topic
SNS sends an email notification to subscribed users
Users must confirm email subscription once during setup

📧 Example Notification:

Student CSV processed successfully and data stored in DynamoDB.

🏗️ Infrastructure as Code

The entire infrastructure is provisioned using AWS CloudFormation:

Resources Created:
S3 Bucket (File upload)
Lambda Function (Processing engine)
DynamoDB Table (Data storage)
SNS Topic (Notification service)
Email Subscription
IAM Roles & Policies
Event Trigger Configuration (S3 → Lambda)
⚙️ Deployment Steps
1️⃣ Deploy CloudFormation Stack
aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name serverless-csv-pipeline \
  --capabilities CAPABILITY_NAMED_IAM
2️⃣ Upload CSV File

Upload students.csv to the S3 bucket.

3️⃣ Execution Flow
S3 triggers Lambda function
Lambda processes CSV data
Data is inserted into DynamoDB
SNS sends email notification
📤 Output Example
DynamoDB Record:
{
  "studentId": "101",
  "name": "John",
  "department": "IT",
  "marks": 85
}
🔐 IAM Permissions

Lambda execution role includes:

s3:GetObject
dynamodb:PutItem
sns:Publish
logs:CreateLogGroup
logs:CreateLogStream
logs:PutLogEvents
⚠️ Challenges Faced
Configuring S3 event triggers correctly
Handling IAM permission issues
Ensuring correct CSV parsing in Lambda
Managing SNS email confirmation workflow
📈 Future Enhancements
Add duplicate record prevention using conditional writes
Move processed files to archive folder in S3
Add failure alerts via SNS
Integrate AWS Glue for advanced ETL processing
Add API Gateway for data querying
📚 Key Learnings
Event-driven serverless architecture on AWS
S3 event notifications and Lambda triggers
DynamoDB NoSQL data modeling
SNS-based notification systems
Infrastructure as Code using CloudFormation
End-to-end cloud data pipeline design
👨‍💻 Author

Saravanan Nadanasabesan
Cloud Computing | Data Engineering | AWS Serverless Architecture

GitHub: https://github.com/
Email: saravanasabesan@gmail.com
LinkedIn: www.linkedin.com/in/saravanan-nadanasabesan-987129107
📜 License

This project is for educational and portfolio purposes only.