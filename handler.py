import boto3, random

def main(event, context):
    # Call the EventBridge Scheduler client from boto3 pkg.
    client = boto3.client('scheduler')

    # Randomize minutes, hours, and days based on preferences/work day.
    minutes = random.choice(['00', '15', '30', '45'])
    hour = random.choice(['10', '11', '12', '13', '14', '15', '16', '17', '18'])
    day = random.choice(['MON','TUE', 'WED', 'THU', 'FRI'])

    # Build the cron expression in AWS's format
    cron_expression = str(f'cron({minutes} {hour} ? * {day} *)')

    # Actually call the update_schedule method from boto3.client
    client.update_schedule(
        Name="name-of-event-schedule",
        FlexibleTimeWindow = {"Mode": "OFF"},
        ScheduleExpressionTimezone='America/New_York',
        Target={
            "Arn": "arn:aws:lambda:etc-etc-etc",
            "RetryPolicy": {"MaximumEventAgeInSeconds": 86400, "MaximumRetryAttempts": 185},
            "RoleArn": "arn:aws:iam::etc-etc-etc",
        },
        ScheduleExpression = cron_expression
    )

if __name__ == "__main__":
    main("", "")
