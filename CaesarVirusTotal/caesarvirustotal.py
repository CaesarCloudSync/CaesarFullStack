import requests
import mimetypes
class CaesarVirusTotal:
    def __init__(self) -> None:
        pass
    def read_file(self,filename,url):
        if filename and not url:
            with open(filename,"rb") as f:
                filedata = f.read()
        elif url and not filename:
            filedata = url
            
        mt = mimetypes.guess_type(filedata)
        if mt:
            print("Mime Type:", mt[0])
            return filedata,mt[0]
        else:
            print("Cannot determine Mime Type")
        
    def scan_file(self,filename=None,url=None):
        filedata,mime = self.read_file(filename,url)
        files = { "file": ("CaesarMongoDB.py", open("download.jpeg", "rb"), "text/x-python") }
        headers = {
            "accept": "application/json",
            "x-apikey": "4d9cc7223e746d02ac6a23125de9092e1855c38001af7efc590ff0b52a06fdb4"
        }

        response = requests.post(url, files=files, headers=headers)

        print(response.text)





import requests

url = "https://www.virustotal.com/api/v3/files/NTVmNDU2MTg2MDQ5MDMwNjdiMWIzOGYwOGQ2NjY3ZDE6MTY4OTg3MTcxNw%3D%3D"

headers = {
    "accept": "application/json",
    "x-apikey": "4d9cc7223e746d02ac6a23125de9092e1855c38001af7efc590ff0b52a06fdb4"
}

response = requests.get(url, headers=headers)

print(response.text)