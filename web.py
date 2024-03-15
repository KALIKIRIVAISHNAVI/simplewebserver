from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<title>TOP 5 SOFTWARE COMPANIES IN REVENUE></title>
</head>
<body>
<table align="center" width="540" cellspacing="2" cellpadding="4" border="5" bgcolor="khaki">
<tr align="center">
           <th bgcolor="olivedrab">S.NO</th>
           <th bgcolor="olivedrab">NAME OF COMPANY</th>
           <th bgcolor="olivedrab">REVENUE</th>
           <th bgcolor="olivedrab">NET INCOME</th>
           <th bgcolor="olivedrab">MARKET CAP</th>
           <th bgcolor="olivedrab">EXCHANGE</th>
           </tr>
           <tr align="center">
           <td>1</td>
           <td>Microsoft Corp. (MSFT)</td>
           <td>$203.08 billion</td>
           <td>$69.79 billio</td>
           <td>$1.82 trillion</td>
           <td>NASDAQ</td>
           </tr>
           <tr align="center">
           <td>2</td>
           <td>Oracle Corp. (ORCL)</td>
           <td> $46.07 billion</td>
           <td> $8.80 billion</td>
           <td>$219.74 billion</td>
           <td>New York Stock Exchange</td>
           </tr>
           </tr>
           <tr align="center">
           <td>3</td>
           <td> SAP SE (SAP)</td>
           <td>$32.97 billion</td>
           <td>$3.52 billion</td>
           <td>$122.57 billion</td>
           <td>New York Stock Exchange</td>
           </tr>
           </tr>
           <tr align="center">
           <td>4</td>
           <td>Salesforce, Inc. (CRM)</td>
           <td> $30.29 billion</td>
           <td> $278 million</td>
           <td> $130.30 billion</td>
           <td>New York Stock Exchange</td>
           </tr>
           </tr>
           <tr align="center">
           <td>5</td>
           <td>Adobe Inc. (ADBE)</td>
           <td> $17.61 billion</td>
           <td>$4.7 billion</td>
           <td> $158.71 billion</td>
           <td>NASDAQ</td>
           </tr>
           </body>
           </html>



"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()