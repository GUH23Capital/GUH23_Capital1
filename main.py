import requests
import json

url = "https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/accounts/create"

payload = json.dumps({
  "quantity": "10",
  "state": "open"
})
headers = {
  'Content-Type': 'application/json',
  'Version': '1.0',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJuYmYiOjE2OTYwMzIwMDAsImFwaV9zdWIiOiJiYWU0MzhjNzkyMWEzNzcxOTZkZGMwNjUxNjExOTg5OTFjZDdiMWIyMzQ2M2RlMzEwYjllYjU5YTU1MWU3NTBkMTcxNzIwMDAwMDAwMCIsInBsYyI6IjVkY2VjNzRhZTk3NzAxMGUwM2FkNjQ5NSIsImV4cCI6MTcxNzIwMDAwMCwiZGV2ZWxvcGVyX2lkIjoiYmFlNDM4Yzc5MjFhMzc3MTk2ZGRjMDY1MTYxMTk4OTkxY2Q3YjFiMjM0NjNkZTMxMGI5ZWI1OWE1NTFlNzUwZCJ9.Ewc9RP9qlXbQW_LPuJg8oX04ctkjnKqUOkVmjkLdw8N23ZdUJdH1BXtILSpIHx9Y5cF39Qs8gWyChMAmI3JVqpqBK7NoCs7yMNhXsxWwhrhNFxTYnLz0MdFB1KqVr1DHO1yNv14r-fM6Yw9ogNQjHHfHPtgEMjHKxF8NQaHYABD24yj9_N0_UxEI3KWCePnsxmMkXp0Oj5YIsXzialJRdQMDBCTN_gkLqSz_5tQqplqB6nF2bWZDEDNqHlRzqG3oHNS8cfnFYPOsANYQqK0y9st196oGKZWCEL-T3VHjB33kzzQUJxHan2mB83dCEcq4BG16xyaD7n84GAmkMktNEA',
  'Cookie': 'AWSALB=pYIxcvLmdzId5LRJFUyt6g+29JaDPTjeI7ot/kcbGiF/aT+cDyaWt018u0UyscM2sSQLV8QjUuh7Mse0bUVjTGbU/OlAbAFxEMwVnu3X3UlkXlrrxzva8i0hLSFs; AWSALBCORS=pYIxcvLmdzId5LRJFUyt6g+29JaDPTjeI7ot/kcbGiF/aT+cDyaWt018u0UyscM2sSQLV8QjUuh7Mse0bUVjTGbU/OlAbAFxEMwVnu3X3UlkXlrrxzva8i0hLSFs'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
