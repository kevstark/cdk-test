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
        queues: List[QueueStack],
        **kwargs
    ) -> None:

        super().__init__(scope, id, **kwargs)

        topic = sns.Topic(
            self, "sns",
            #display_name="My First Topic"
        )
        for i, q in enumerate(queues):
            self.add_dependency(q)
            qarn = core.Fn.import_value(f"{q.stack_name}-queuearn")
            qq=sqs.Queue.from_queue_arn(self, f'q{i}', qarn)
            topic.add_subscription(subs.SqsSubscription(qq))


        core.CfnOutput(
            self, "sns_arn",
            value=topic.topic_arn
        )
