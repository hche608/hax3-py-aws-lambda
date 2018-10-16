from basicLambda import fetch

print("Loading function")


def lambda_handler(event, context):
    print(event)
    print(context)
    url = 'https://www.google.co.nz/'
    return fetch(url)
