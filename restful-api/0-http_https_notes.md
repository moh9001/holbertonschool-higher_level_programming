# ✅ Task 0: Basics of HTTP/HTTPS

---

## 🔒 HTTP vs HTTPS

| Aspect        | HTTP                              | HTTPS                                |
|---------------|-----------------------------------|---------------------------------------|
| **Security**  | No encryption                     | Encrypted using SSL/TLS              |
| **Port**      | Default is 80                     | Default is 443                       |
| **Use Case**  | Safe for general browsing         | Required for login, payment, forms   |
| **Padlock**   | ❌ No browser padlock              | ✅ Padlock appears in browser         |
| **Vulnerable**| Susceptible to sniffing, MITM     | Data is protected from eavesdropping |

> 🔑 **Key Point**: HTTPS encrypts all communication between client and server, making it secure from attackers.

---

## 🔁 Structure of HTTP Requests and Responses

### 📨 HTTP Request Example:

GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html


### 📬 HTTP Response Example:

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 305

<html> ... </html> ```
Summary:

Request = Method + Path + Headers

Response = Status Line + Headers + Body


🔧 Common HTTP Methods
Method	Description	Use Case
GET	Retrieve data	Fetch a webpage, or data from an API
POST	Submit data	Submit a form, or create a resource
PUT	Update a resource	Replace a user’s full profile
DELETE	Remove a resource	Delete a blog post or user


📡 Common HTTP Status Codes
Code	Name	Description & Use Case
200	OK	The request was successful
201	Created	New resource was successfully created
400	Bad Request	The request has syntax or validation errors
401	Unauthorized	Authentication is required (invalid/missing)
404	Not Found	Resource could not be found on the server
500	Internal Server Error	Something went wrong on the server
