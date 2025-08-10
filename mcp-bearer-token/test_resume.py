import requests

url = "http://127.0.0.1:8086/tools/verify_resume"
data = {
    "name": "Mokksh",
    "target_role": "AI Engineer"
}
files = {
    "file": open("resume.pdf", "rb")  # Replace with your actual file path
}

response = requests.post(url, data=data, files=files)
print(response.json())