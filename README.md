# eventbridge-randomizer
The most simple script possible to randomize an eventbridge schedule!

We wanted to make a random messaging service in our organization, and I decided to use an AWS Lambda function. 
Coupled with EventBridge, you are able to invoke Lambda functions on a schedule but not randomly (because who else ever needs that?).
So this is just one small piece of the application I built. I hope this is helpful or at least entertaining to you.

If you're going to use this, I recommend using the AWS EventBridge API to pull "Target" as it currently is setup on your Event. Just makes life easier.
