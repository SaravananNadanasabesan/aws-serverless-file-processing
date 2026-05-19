🚀 AWS Serverless CSV Processing Pipeline (S3 → Lambda → DynamoDB + SNS)
📌 Project Overview

This project demonstrates a fully serverless event-driven data pipeline using AWS services. A CSV file uploaded to an Amazon S3 bucket automatically triggers an AWS Lambda function. The Lambda function processes the file, stores structured records in Amazon DynamoDB, and sends an email notification using Amazon SNS upon successful processing.

This architecture ensures automated data ingestion, real-time processing, and event-based notifications without any manual intervention.

🏗️ Architecture
S3 Bucket (CSV Upload)
        ↓ (Event Trigger)
AWS Lambda Function
        ↓
 ┌─────────────────────────────┐
 ↓                             ↓
Amazon DynamoDB           Amazon SNS
                               ↓
                        Email Notification
⚙️ AWS Services Used
🪣 Amazon S3 – Stores uploaded CSV files
⚡ AWS Lambda – Processes and transforms CSV data
🗄️ Amazon DynamoDB – Stores structured student records
📣 Amazon SNS – Sends email notifications
🔐 AWS IAM – Manages secure permissions
📊 Amazon CloudWatch – Logs and monitoring
🧱 Infrastructure as Code (CloudFormation)

The entire infrastructure is deployed using AWS CloudFormation, including:

S3 bucket for file uploads
DynamoDB table for data storage
Lambda function for processing
SNS topic + email subscription
IAM roles and permissions
S3 → Lambda trigger configuration
📄 Sample Dataset (CSV)
studentId,name,department,marks
101,John,IT,85
102,Alice,CSE,91
103,Bob,ECE,78
🗄️ DynamoDB Table Schema
Attribute	Type	Description
studentId	String	Primary Key
name	String	Student name
department	String	Department
marks	Number	Student marks
🔔 SNS Email Notification Flow
📌 How it works:
Lambda processes CSV successfully
Lambda publishes message to SNS topic
SNS sends email to subscribed users
📧 SNS Setup (Included in CloudFormation)
SNS Topic: StudentProcessingTopic
Subscription Protocol: Email
Endpoint: User-defined email

👉 After deployment, you must confirm the subscription email.

⚙️ Lambda Function Logic

The Lambda function performs the following steps:

Triggered by S3 upload event
Reads CSV file from S3 bucket
Parses file using Python csv module
Inserts each row into DynamoDB using put_item()
Sends SNS notification after successful processing
🧾 CloudFormation Features

This project uses Infrastructure as Code (IaC) to provision:

✔ S3 Bucket
✔ DynamoDB Table
✔ Lambda Function
✔ SNS Topic + Subscription
✔ IAM Roles & Policies
✔ S3 → Lambda trigger permission

🔐 IAM Permissions Required

Lambda execution role includes:

s3:GetObject
dynamodb:PutItem
sns:Publish
logs:CreateLogGroup
logs:CreateLogStream
logs:PutLogEvents
🧪 How to Deploy & Test
🚀 Step 1: Deploy CloudFormation Stack

Provide:

LambdaCodeBucket
LambdaCodeKey
NotificationEmail
📤 Step 2: Upload CSV File

Upload students.csv to the S3 bucket.

⚡ Step 3: Automatic Execution
S3 triggers Lambda
Data is inserted into DynamoDB
SNS email is sent
📊 Step 4: Verify Output

Check:

CloudWatch logs (Lambda execution)
DynamoDB table (inserted records)
Email inbox (SNS notification)
🚨 Common Issues & Fixes
❌ Lambda not triggered
Check S3 event notification configuration
Ensure correct bucket and region
❌ No data in DynamoDB
Verify IAM permissions
Check CloudWatch logs
Validate CSV parsing logic
❌ No email received
Confirm SNS subscription email
Check spam/junk folder
Ensure sns:Publish permission is enabled
📈 Future Enhancements
Add duplicate record prevention (conditional writes)
Move processed files to S3 archive folder
Add SNS failure alerts for errors
Integrate AWS Glue for advanced transformation
Add API Gateway for querying student data
👨‍💻 Author

Saravanan Nadanasabesan
Cloud Computing & Data Engineering Enthusiast 🇨🇦

📜 License

This project is for educational purposes only.