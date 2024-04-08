import azure.functions as func
import logging
import json

app = func.FunctionApp()

@app.function_name(name="cosmos_db_reader")
@app.route(route="GetResumeCounter", auth_level=func.AuthLevel.ANONYMOUS)
@app.cosmos_db_input(arg_name="documents", 
                     database_name="AzureResume",
                     container_name="Counter", 
                     connection="CosmosDbConnectionSetting"
                     )
@app.cosmos_db_output(arg_name="outDocument",
                      database_name="AzureResume",
                      container_name="Counter",
                      connection="CosmosDbConnectionSetting"
                      )

def cosmos_db_reader(req: func.HttpRequest, documents: func.DocumentList, outDocument: func.Out[func.Document]) -> func.HttpResponse:
    newdocument = documents[0]
    newdocument["count"] = newdocument.get('count',0) + 1
    outDocument.set(newdocument)
    logging.info(f' {newdocument.get("count",0)}')
    return func.HttpResponse(
        body=json.dumps({"count": newdocument.get("count",0)}),
        status_code=200,
        headers={"Content-Type": "application/json"}
    )