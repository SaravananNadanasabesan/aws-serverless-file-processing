# ☁️ Serverless CSV Processing Pipeline (AWS S3 + Lambda + DynamoDB + SNS)

---

## 📌 Project Overview

This project was developed as part of a **Cloud Computing & Data Engineering learning track**.

The objective is to design and implement a **fully serverless data processing pipeline on AWS** that automatically processes CSV files uploaded to Amazon S3, stores structured data in DynamoDB, and sends real-time email notifications using SNS.

### 🔧 Key Capabilities
- Event-driven data ingestion using S3  
- CSV processing using AWS Lambda  
- Structured data storage in DynamoDB  
- Real-time notifications using SNS  
- Infrastructure automation using CloudFormation (IaC)  

---

## 🎯 Project Goal

To eliminate manual data processing and build a **scalable, automated cloud-native pipeline** for handling structured CSV data.

### ✔️ System Benefits
- Fully automated file processing  
- Real-time data persistence  
- Notification-based monitoring  
- Highly scalable serverless architecture  
- Infrastructure as Code (IaC)  

---

## 🚩 Business Problem

Organizations often face challenges such as:

- Manual processing of uploaded files  
- Delayed data availability for analytics  
- Lack of real-time ingestion notifications  
- Error-prone data entry workflows  
- Difficulty scaling traditional ETL systems  

### 💡 Solution
This project solves these challenges using an **event-driven AWS serverless architecture**.

---

## 👨‍💻 My Role

**Cloud Developer – Serverless Data Pipeline Implementation**

### Responsibilities
- Designed AWS serverless architecture  
- Developed Lambda function for CSV processing  
- Configured S3 event triggers  
- Designed DynamoDB schema for structured storage  
- Integrated SNS for email notifications  
- Built CloudFormation templates (IaC)  
- Configured IAM roles and permissions  

---

## 🏗️ Solution Architecture

### 🔹 AWS Components

- **Amazon S3** → File storage & event trigger  
- **AWS Lambda** → CSV processing engine  
- **Amazon DynamoDB** → NoSQL data storage  
- **Amazon SNS** → Notification service  
- **AWS IAM** → Security & access control  
- **AWS CloudFormation** → Infrastructure as Code  

---

## 📊 Dataset

```csv
studentId,name,department,marks
101,John,IT,85
102,Alice,CSE,91
103,Bob,ECE,78
```
## 🗄️ DynamoDB Schema

| Field      | Type   | Key Type      |
| ---------- | ------ | ------------- |
| studentId  | String | Partition Key |
| name       | String | -             |
| department | String | -             |
| marks      | Number | -             |


## 🔔 Notification System (SNS)
Workflow
CSV uploaded to S3
Lambda processes the file
Data stored in DynamoDB
SNS publishes notification
Email sent to subscribed users

## 📧 Example Notification:

Student CSV processed successfully and data stored in DynamoDB.

## 🏗️ Infrastructure as Code (CloudFormation)

All infrastructure is deployed using AWS CloudFormation.

Resources Provisioned
S3 Bucket (File ingestion)
Lambda Function (Processing engine)
DynamoDB Table (Data storage)
SNS Topic (Notifications)
IAM Roles & Policies
S3 → Lambda event trigger

## ⚙️ Deployment Steps
1️⃣ Deploy Stack
aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name serverless-csv-pipeline \
  --capabilities CAPABILITY_NAMED_IAM
2️⃣ Upload File

Upload students.csv to the S3 bucket.

3️⃣ Execution Flow
S3 triggers Lambda
Lambda processes CSV
Data inserted into DynamoDB
SNS sends email notification

## 📤 Output Example
{
  "studentId": "101",
  "name": "John",
  "department": "IT",
  "marks": 85
}

## 🔐 IAM Permissions
s3:GetObject
dynamodb:PutItem
sns:Publish
logs:CreateLogGroup
logs:CreateLogStream
logs:PutLogEvents

## ⚠️ Challenges Faced
Configuring S3 event triggers correctly
Managing IAM permissions for Lambda
Parsing CSV data in Lambda
Handling SNS email subscription flow

## 📈 Future Enhancements
Add duplicate record prevention (conditional writes)
Archive processed files in S3
Add failure alerts via SNS
Integrate AWS Glue for advanced ETL pipelines
Add API Gateway for querying data

## 📚 Key Learnings
Event-driven serverless architecture
AWS S3 → Lambda integration
DynamoDB NoSQL design principles
SNS messaging system
Infrastructure as Code (CloudFormation)
End-to-end cloud data pipeline design

## 👨‍💻 Author

Saravanan Nadanasabesan
Cloud Computing | Data Engineering | AWS Serverless Architecture

GitHub: https://github.com/SaravananNadanasabesan
LinkedIn: https://www.linkedin.com/in/saravanan-nadanasabesan-987129107
Email: saravanasabesan@gmail.com