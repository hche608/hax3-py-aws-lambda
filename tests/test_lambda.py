from basicLambda import awslambda


def test_lambda_handler():
    assert awslambda.lambda_handler("event", "context") == "Job's done"
