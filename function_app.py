import logging

import azure.functions as func

from prediction import make_prediction

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="predict")
def predict(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    tenure = req.params.get('tenure')
    monthly = req.params.get('monthly')
    techsupport = req.params.get('techsupport')

    prediction = make_prediction(
        tenure=tenure,
        MonthlyCharges=monthly,
        TechSupport_yes=techsupport
    )
    if tenure and monthly and techsupport:
        return func.HttpResponse(f"Hello, the probability that this customer will churn is {prediction}.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a tenure, monthly and techsupport to get a prediction.",
             status_code=200
        )