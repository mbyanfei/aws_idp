#!/usr/bin/env python3
import aws_cdk as cdk

from textract_cdk_stack_samples.demo_with_queries_stack import DemoQueries

app = cdk.App()

DemoQueries(app, "IDP-Textract-Queries2rfr7")

app.synth()
