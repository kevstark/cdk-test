from typing import List
from aws_cdk import (
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    core
)
from src import QueueStack

class JoinStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str,
        queue_arn: List[str],
        **kwargs
    ) -> None:

        super().__init__(scope, id, **kwargs)

        topic = sns.Topic(
            self, "sns",
            #display_name="My First Topic"
        )
        for q in queue_arn:
            qq = sqs.Queue.from_queue_arn(self, 'q1', q)
            topic.add_subscription(subs.SqsSubscription(qq))


        core.CfnOutput(
            self, "sns_arn",
            value=topic.topic_arn
        )
