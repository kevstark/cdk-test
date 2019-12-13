#!/usr/bin/env python3
import datetime as datetime
from aws_cdk import core

from src import (QueueStack, JoinStack)


app = core.App()

q1 = QueueStack(app, 'Test1')
#q2 = QueueStack(app, 'Test2')

j1 = JoinStack(app, 'JoinA', queue_arn=[q1.queue.queue_arn])
j1.add_dependency(q1)
app.synth()
