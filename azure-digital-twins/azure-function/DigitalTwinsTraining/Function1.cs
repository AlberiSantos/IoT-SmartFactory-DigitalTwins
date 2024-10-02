// Default URL for triggering event grid function in the local environment.
// http://localhost:7071/runtime/webhooks/EventGrid?functionName={functionname}

using System;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.EventGrid;
using Microsoft.Extensions.Logging;
using Azure.Messaging.EventGrid;
using Azure;
using Azure.Core.Pipeline;
using Azure.Identity;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json;
using System.Threading.Tasks;
using System.Net.Http;
using Azure.DigitalTwins.Core;


namespace DigitalTwinsTraining
{
    public class Function1
    {
        private static readonly HttpClient httpClient = new HttpClient();
        private static string adtServiceUrl = Environment.GetEnvironmentVariable("ADT_SERVICE_URL");  //This will be populated at runtime by the environment variable you set up earlier for the Azure function app. adtServiceUrl will ultimately be set to "https://<host-name-of-your-Azure-Digital-Twins-instance>".

        [FunctionName("IoTHubToADT")]

        public async Task Run([EventGridTrigger] EventGridEvent eventGridEvent, ILogger log)
        {
            log.LogInformation(eventGridEvent.Data.ToString());

            var credentials = new DefaultAzureCredential();
            DigitalTwinsClient client = new DigitalTwinsClient(
                new Uri(adtServiceUrl), credentials, new DigitalTwinsClientOptions
                { Transport = new HttpClientTransport(httpClient) });
            log.LogInformation($"Conexão com o cliente ADT criada.");

            if (eventGridEvent != null && eventGridEvent.Data != null)
            {
                try
                {
                    log.LogInformation(eventGridEvent.Data.ToString());

                    // Decodificar a mensagem de base64
                    JObject deviceMessage = JObject.Parse(eventGridEvent.Data.ToString());
                    string body = deviceMessage["body"].ToString();
                    string decodedBody = System.Text.Encoding.UTF8.GetString(Convert.FromBase64String(body));
                    log.LogInformation($"Mensagem decodificada: {decodedBody}");

                    // Parse a mensagem JSON
                    JObject oeeMessage = JObject.Parse(decodedBody);
                    double oee = (double)oeeMessage["OEE"];
                    log.LogInformation($"OEE: {oee}");

                    // Definir o ID do gêmeo digital a ser atualizado
                    string twinId = "FLM1_Esteira1_OEE";

                    // Criar um documento JSON Patch para atualizar a propriedade "value"
                    var updateTwinData = new JsonPatchDocument();
                    updateTwinData.AppendReplace("/value", oee.ToString());
                    updateTwinData.AppendReplace("/valueUnitOfMeasure", "%");

                    // Atualizar o gêmeo digital
                    await client.UpdateDigitalTwinAsync(twinId, updateTwinData);
                    log.LogInformation($"Gêmeo digital {twinId} atualizado com o valor do OEE.");
                }
                catch (Exception ex)
                {
                    log.LogError($"Erro ao processar o evento: {ex.Message}");
                    throw;
                }
            }
        }
    }
}
