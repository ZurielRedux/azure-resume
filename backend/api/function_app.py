import azure.functions as func
import logging
import json

app = func.FunctionApp()

@app.function_name(name="cosmos_db_reader")
@app.route(route="http_trigger", auth_level=func.AuthLevel.ANONYMOUS)
@app.cosmos_db_input(arg_name="documents", 
                     database_name="AzureResume",
                     container_name="Counter", 
                     #id="1", 
                     connection="CosmosDbConnectionSetting"
)

def cosmos_db_reader(req: func.HttpRequest, documents: func.DocumentList) -> func.HttpResponse:
    document = str(documents[0]["count"]+1)
    logging.info(document)
    return func.HttpResponse(
        document,
        status_code=200
    )
    
