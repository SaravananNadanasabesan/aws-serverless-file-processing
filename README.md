📦 Serverless CSV Processing Pipeline (AWS)

Event-driven data pipeline using AWS S3, Lambda, DynamoDB, and SNS with Infrastructure as Code (CloudFormation)

📌 Overview

This project implements a fully serverless AWS pipeline where CSV files uploaded to an S3 bucket automatically trigger a Lambda function. The function processes the data, stores it in DynamoDB, and sends an email notification via SNS upon successful execution.

The system is deployed using AWS CloudFormation (Infrastructure as Code).

🏗️ Architecture
S3 (CSV Upload)
      ↓
Lambda (Event Trigger)
      ↓
DynamoDB (Data Storage)
      ↓
SNS (Email Notification)
⚙️ AWS Services
Amazon S3 – File storage and event source
AWS Lambda – Serverless compute for processing CSV
Amazon DynamoDB – NoSQL database for structured data
Amazon SNS – Email notification service
AWS IAM – Access control and permissions
AWS CloudFormation – Infrastructure as Code
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
Subscription confirmation is required once during setup

Event Example:

“Student CSV processed successfully and data inserted into DynamoDB.”

⚙️ Infrastructure as Code (CloudFormation)

All AWS resources are provisioned using CloudFormation:

Includes:
S3 Bucket (CSV upload)
Lambda Function (CSV processor)
DynamoDB Table (data storage)
SNS Topic (notifications)
Email subscription
IAM Roles & policies
S3 → Lambda trigger permission
🚀 Deployment Workflow
1. Deploy Stack

Provide parameters:

LambdaCodeBucket
LambdaCodeKey
NotificationEmail
aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name csv-pipeline-stack \
  --capabilities CAPABILITY_NAMED_IAM
2. Upload CSV

Upload students.csv to the S3 bucket.

3. Automatic Processing

Once uploaded:

S3 triggers Lambda
Lambda processes CSV
Data is stored in DynamoDB
SNS sends email notification
📤 Expected Output
DynamoDB Record Example:
{
  "studentId": "101",
  "name": "John",
  "department": "IT",
  "marks": 85
}
SNS Email:

Student CSV processed successfully and data inserted into DynamoDB.

🔐 IAM Permissions

Lambda execution role includes:

s3:GetObject
dynamodb:PutItem
sns:Publish
logs:CreateLogGroup
logs:CreateLogStream
logs:PutLogEvents
⚠️ Known Issues / Notes
SNS email subscription must be confirmed manually
Ensure S3 event trigger is enabled for .csv files
DynamoDB requires correct primary key mapping (studentId)
📈 Future Improvements
Add duplicate record prevention using conditional writes
Move processed files to an archive S3 folder
Add failure alerts using SNS
Integrate AWS Glue for transformation layer
Expose data via API Gateway
👨‍💻 Author

Saravanan Nadanasabesan
Cloud & Data Engineering | AWS | Serverless Architectures

📜 License

This project is intended for educational and portfolio purposes.

⭐ Project Highlights

✔ Fully serverless architecture
✔ Event-driven processing
✔ Infrastructure as Code (CloudFormation)
✔ Real-time notifications via SNS
✔ Scalable AWS design pattern