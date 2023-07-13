import boto3, random

def main(event, context):
    client = boto3.client('scheduler')

    minutes = random.choice(['00', '15', '30', '45'])
    hour = random.choice(['10', '11', '12', '13', '14', '15', '16', '17', '18'])
    day = random.choice(['MON','TUE', 'WED', 'THU', 'FRI'])

    cron_expression = str(f'cron({minutes} {hour} ? * {day} *)')

    client.update_schedule(
        Name="name-of-event-schedule",
        FlexibleTimeWindow = {"Mode": "OFF"},
        Target={
            "Arn": "arn:aws:lambda:etc-etc-etc",
            "RetryPolicy": {"MaximumEventAgeInSeconds": 86400, "MaximumRetryAttempts": 185},
            "RoleArn": "arn:aws:iam::etc-etc-etc",
        },
        ScheduleExpression = cron_expression
    )

if __name__ == "__main__":
    main("", "")
