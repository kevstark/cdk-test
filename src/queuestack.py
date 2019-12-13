from aws_cdk import (
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    core
)


class QueueStack(core.Stack):

    def __init__(self, app: core.App, id: str, **kwargs) -> None:
        super().__init__(app, id, **kwargs)

        self.queue = sqs.Queue(
            self, "sqs",
            visibility_timeout=core.Duration.seconds(300),
        )

        core.CfnOutput(
            self, "queue_arn",
            value = self.queue.queue_arn,
            export_name=f"{self.stack_name}-queuearn"
        )
