# Project-8-Insert-Fetch-Google-Sheets-API

### Base URL 
```http://testingapps.pythonanywhere.com/```

### Endpoints

#### 1. ```/api/insert/```
  #### Method : POST
  #### Request
  ```json
  {
      "uid":"21BCS9973",
      "name":"Ritik",
      "email":"21BCS9973@cuchd.in",
      "section":646,
      "group":"B",
      "yearOfGraduation":"2025",
      "experience":"Yes",
      "phoneNumber":9369130228,
      "team":"AI Card",
      "role":"Team Lead",
      "introduction":"I am good, how are you?",
      "previousProjects":"Redirect to my GitHub",
      "resumeLink":"link"
  }
  ```
  #### Response
  ```json
  {
      "message": "Saved successfully.",
      "success": true
  }
  ```
#### 2. ```/api/fetch/?uid=21BCS9973```
  #### Method : GET
  #### Response
  ```json
  {
      "message": "Record Found.",
      "data": {
          "UID": "21BCS9973",
          "Name": "Ritik",
          "Email": "21BCS9973@cuchd.in",
          "Section": 646,
          "Group": "B",
          "Year of Graduation": 2025,
          "Experience": "Yes",
          "Phone Number": 9369130228,
          "Team": "AI Card",
          "Role": "Team Lead",
          "Introduction": "I am good, how are you?",
          "Previous Projects": "Redirect to my GitHub",
          "Resume Link": "link"
      },
      "success": true
  }
  ```
