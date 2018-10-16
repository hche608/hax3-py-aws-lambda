from basicLambda import fetch
from mockito import when, mock, verifyStubbedInvocationsAreUsed
import requests


def test_fetch():
    url = 'https://example.com/'
    response = mock({'text': 'Ok'}, spec=requests.Response)
    session = mock(requests.Session)

    # Given
    # `when` here configures the mock
    when(session).get(url).thenReturn(response)
    # `when` *patches* the globally available *requests* module
    when(requests).Session().thenReturn(session)  # <=

    # When
    res = fetch(url)

    # Then
    assert res.text == 'Ok'

    # no need to verify anything here, if we get the expected response
    # back, `url` must have been passed through the system, otherwise
    # mockito would have thrown.
    # We *could* ensure that our mocks are actually used, if we want:
    verifyStubbedInvocationsAreUsed()
