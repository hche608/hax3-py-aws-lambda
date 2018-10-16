from basicLambda import awslambda, fetch
from mockito import when, mock, verifyStubbedInvocationsAreUsed
import requests


def test_lambda_handler():
    url = 'https://www.google.co.nz/'
    response = mock({'text': 'Ok'}, spec=requests.Response)
    # Given
    when(awslambda).fetch(url).thenReturn(response)
    # When
    actual = awslambda.lambda_handler("event", "context")
    # Then
    assert actual.text == 'Ok'
