📌 Overview

This project implements a fully serverless AWS pipeline where CSV files uploaded to an S3 bucket automatically trigger a Lambda function.

The function processes the data, stores it in DynamoDB, and sends an email notification via SNS upon successful execution.

The entire infrastructure is provisioned using AWS CloudFormation (IaC).

🏗️ Architecture
S3 (CSV Upload)
   ↓
Lambda (Trigger)
   ↓
DynamoDB (Storage)
   ↓
SNS (Email Notification)
⚙️ AWS Services Used
Amazon S3 → File storage & event trigger
AWS Lambda → Serverless processing
Amazon DynamoDB → NoSQL data storage
Amazon SNS → Email notifications
AWS IAM → Security & permissions
CloudFormation → Infrastructure as Code
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
🔔 SNS Notification Flow

After successful processing:

Lambda processes CSV
Data is inserted into DynamoDB
SNS publishes a message
Email is sent to subscribed users

📧 Example message:

Student CSV processed successfully and data stored in DynamoDB.

🏗️ Infrastructure as Code

All AWS resources are created using CloudFormation:

S3 Bucket
Lambda Function
DynamoDB Table
SNS Topic + Email Subscription
IAM Roles & Policies
S3 → Lambda trigger
🚀 Deployment Steps
1️⃣ Deploy Stack
aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name csv-pipeline \
  --capabilities CAPABILITY_NAMED_IAM
2️⃣ Upload CSV

Upload students.csv to S3 bucket.

3️⃣ Execution Flow
S3 triggers Lambda
Lambda processes file
Data stored in DynamoDB
SNS sends email notification
📤 Output Example
DynamoDB Item
{
  "studentId": "101",
  "name": "John",
  "department": "IT",
  "marks": 85
}
⚠️ Common Issues
SNS email must be confirmed manually
S3 event trigger must allow .csv
IAM permissions must include sns:Publish
📈 Future Enhancements
Duplicate record prevention
Move processed files to archive folder
Failure alerts via SNS
API Gateway integration
👨‍💻 Author

Saravanan Nadanasabesan
Cloud & Data Engineering | AWS Serverless

📜 License

This project is for educational purposes only.