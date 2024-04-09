window.addEventListener('DOMContentLoaded', event => {
    getVisitCount();
})

const functionApiUrl = 'https://zurielpythonfunctionapp.azurewebsites.net/api/GetResumeCounter?';
const localFunctionApi = 'http://localhost:7071/api/GetResumeCounter';

const getVisitCount = () => {
    let count = 30;
    fetch(functionApiUrl).then(Response => {
        return Response.json()
    }).then(Response => {
        console.log("Website called function API.");
        count = Response.count;
        document.getElementById("counter").innerText = count;
    }).catch(function(error){
        console.log(error);
    });
    return count;
}