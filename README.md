### Project information

This solution deploys a workflow to demonstrate how extract information from documents using the Amazon Textract Queries features. The project uses the [Python AWS Cloud Development Kit (CDK)](https://aws.amazon.com/cdk/) to deploy 

### Architecture Overview

The architecture is based entirely on serverless components. 
The document processing is realized through a AWS Step Functions workflow, which is triggered when an object is put in the S3 bucket under the 'uploads' prefix.

The tasks in the workflow execute AWS Lambda Functions.

![Amazon Step Functions workflow for Textract Queries ](https://raw.githubusercontent.com/aws-samples/amazon-textract-idp-cdk-stack-samples/main/images/DemoQueries_graph.svg)

For more information on the general concepts and a walkthrough check out the ['Document Processing at Scale' workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/f2dd7c46-e022-4f9c-8399-dcad742be516/en-US)

### Connections and permissions

You can create a new account connection from the AWS accounts menu in your Amazon CodeCatalyst space. AWS IAM roles added to the account connection are used to authorize project workflows to access AWS account resources.

Expected role capabilities: CodeCatalyst*

### Project resources

This project contains the following folders:

* lambda - 2 Lambda functions, one to generate a random number and one to trigger the start of a Step Functions workflow.
* textract_cdk_stack_samples - The CDK stack definition

This project has created the following Amazon CodeCatalyst Resources:

*     A source repository
*     An environment
*     A workflow for deploying changes pushed to main at .codecatalyst/workflows/onPushToMainDeployPipeline.yaml

### Cleaning up resources

All resources as part of the solution are deployed through CloudFormation and can be removed by deleting the stack.
If you want to delete from command line, go to the root folder of the application and type 

```
cdk destroy IDP-Textract-Queries2rfr7 
```
### CDK Deployment

If you want to deploy without using CI/CD workflows, go to the root folder of the application and type 

```
cdk deploy IDP-Textract-Queries2rfr7 
```

### Additional Resources

[Amazon Textract - IDP document processing at scale workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/f2dd7c46-e022-4f9c-8399-dcad742be516/en-US)

[Amazon Textract IDP CDK Stack Samples](https://github.com/aws-samples/amazon-textract-idp-cdk-stack-samples#demo-queries) on which is workflow is based on

[Amazon Textract IDP CDK Constructs](https://github.com/aws-samples/amazon-textract-idp-cdk-constructs) on which the IDP CDK Stack Samples are build on

[Amazon Textract Queries blog post](https://aws.amazon.com/blogs/machine-learning/specify-and-extract-information-from-documents-using-the-new-queries-feature-in-amazon-textract/)

[Amazon Textract AnalyzeDocument API](https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html)
