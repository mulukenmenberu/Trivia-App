# Trivia API  - Backend Documentation
## Environemnt Setum & Setting up the Backend
### Python Installation 
If you Don't have installed Python yet, please go here and itstall it. 
https://docs.python.org/3/using/unix html#getting-and-installing-the-latest-version-of-python)

### Creating Virtual Environemnt 
  **Creating Virtual Environment on Linux** - 
  ```bash
python3 -m venv venv
```
  **Activating Virtual Environment on Linux** - 
  ```bash
source venv/bin/activate
```
 **Creating Virtual Environment on Windows** - 

### Installing Dependencies
  all required packages are found in requirements.txt. so, after switching to your vertual ebvironemnt, run the following command to install all required packages 

  ```bash
  pip install -r requirements.txt
  ```

### Set up the Database
connect to your postgres database engine and run the following command to create the database.

```bash
createbd trivia
```
### Importing demo data to the Database
If you want to have a demo data in the newly created DB, you can run the following command. The demo DB file located under this directory. 

```bash
psql trivia < trivia.psql
```
### Exporting Environment Variables 
In order to run this flask API, please run the following command to store your root app to environemnt variable 
```bash
export FLASK_APP=flaskr/
```
### Run the Server

To run the server, execute:

```bash
flask run
```
### API Description 

### Endponints accessed by GET Method 
  1.  /questions
      - gets list of questions based on  pagination. List of questions under the specified page will be listed 
      - Request Arguments: Page ID
      - Returns JSON data like the following format 
      ```json
              {

                "questions": "list of formatted question details",
                "total_questions":"questions_count",
                "categories": "category_array",
                "current_category": "current_catagory"
            
          } 
  2. /categories
      - gets list of categories. 
          - Request Arguments: None
          - Returns JSON data like the following format 
          ```json
                  {
                  "categories":{"1":"Science","2":"Geography"....}
                  }
  3. /categories/<int:category_id>/questions
      - gets list of questions based on  catagory. list of questions that match witht he selected category will be returned. 
          - Request Arguments: Category
          - Returns JSON data like the following format 
          ```json
                  {

                    "questions": "list of formatted question details",
                    "total_questions":"questions_count",
                    "categories": "category_array",
                    "current_category": "current_catagory"
                
              } 
  4. /quizzes
        - retrives one question at a time based on some random function either in a selected category or from all categories. 
          - Request Arguments: previous_questions, quiz_category
                - se example below
                ```json 
                    {
                      {"previous_questions": [], "quiz_category": {"type": "Geography", "id": "3"}}
                    }
          - Returns JSON data like the following format 
          ```json
                     {
                    "question":{"id": "question_id", "question":"question text", "answer":"answer", "difficulty":"difficulty", "category":"category"

                   }
### Endponints accessed by POST Method 
  1. /questions
  2. /questions/search
      - gets list of questions based on  search condition. list of questions that match partially or fully with the search condition will be returned. 
      - Request Arguments: Search string 
      - Returns JSON data like the following format 
      ```json
              {

                "questions": "list of formatted question details",
                "total_questions":"questions_count",
                "categories": "category_array",
                "current_category": "current_catagory"
            
          } 
### Endponints accessed by DELETE Method 
  1. /questions/<int:question_id>
    - Deletes a question based on ID
          - Request Arguments: Question ID
          - Returns success message like the following format 
          ```json
              {
            "message":"question deletedess"
              }

