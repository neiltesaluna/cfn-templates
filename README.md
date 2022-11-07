# cfn-templates
This repository contains a bunch of CloudFormation to create different types of Amazon resources. 

These template snippets are also a showcase on some of the things I've played around with on AWS to provide the necessary infrastructure to Projects I've created

### Deploying the templates using AWS CLI
To deploy these templates using AWS CLI we need to run the following command in our terminal:
`aws cloudformation deploy --template-file s3-lambda-cfn.yml --stack-name s3-lambda-stack --capabilities CAPABILITY_NAMED_IAM`

`--template-file (string)`: *The  path where your AWS CloudFormation template is located.*

`--stack-name (string)`: *The name of the AWS CloudFormation  stack  you're deploying to. If you specify an existing stack, the command updates the stack. If you specify a new stack, the command creates it.*

`--capabilities CAPABILITY_NAMED_IAM`: *If you have IAM resources with custom names such as `RoleName`, you must specify `CAPABILITY_NAMED_IAM`.*