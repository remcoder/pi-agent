import http.client, urllib
import sys
import json


def sendViaPushover(message):
  conn = http.client.HTTPSConnection("api.pushover.net:443")
  conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
      "token": "<token>",
      "user": "<user_key>",
      "message": message,
    }), { "Content-type": "application/x-www-form-urlencoded" })
  resp = conn.getresponse()
    
  # Get the status code
  status_code = resp.status
  print(f"Response Status Code: {status_code}")
  
  # Optionally, read and print the response body
  # Useful for debugging or confirming successful delivery
  response_body = resp.read()
  print(f"Response Body: {response_body.decode('utf-8')}")
  
  # Ensure the connection is closed
  conn.close()
  
  # Return status code for further handling if needed
  return status_code

if __name__ == "__main__":
    try:
      report = json.load(sys.stdin)
    except:
      print("Notify: error reading json input")
      sys.exit(1)
    
    alert_status = report.get('alert_status')
    descriptive_report = report.get('descriptive_report')
    sys.stderr.write('Sending report\n')
    sys.stderr.flush()
    sendViaPushover(descriptive_report)
