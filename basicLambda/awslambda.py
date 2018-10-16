print("Loading function")


def lambda_handler(event, context):
    print(event)
    print(context)
    if context is not None:
        return "Job's done"
    return "Job's not done"
