# ETL pipeline Automation With Airflow
This project focuses on automating a workflow. The workflow fetches semi-structured data from an API
every two (2) minutes, transforms it into a structured format, and dumps the data into a PostgreSQL database.


Please follow these steps to enable you run the project seamlessly:

1.  Clone the repository
2.  Make sure you have Docker and PostgreSQL installed.
3.  Open Docker and make sure the Docker engine is running. 
4.  Open PostgreSQL and be sure it's up and running.
5.  Open the "postgres_db_credentials.txt" file in the repository and set your PostgreSQL database credentials.
6.  Navigate through the Airflow folder into the dags folder. Locate the "db_config_airflow.txt" file and set 
    the credentials for the PostgreSQL database. NB: For this specific file, please bear in mind that this is what your localhost
    should be set to : "host.docker.internal"
7.  Open and run the etl_pipeline.py file.
8.  After the execution check your Postgres database to be sure a table named jokes_data has been created
    and populated with 10 rows of data from the API. 	
7.  Open up your cmd/terminal and navigate to the cloned repository. Make sure you are inside the repository at
    the first level. eg: **C:\Program Files\GitHub\ETL-Automation-With-Airflow>**		 
8.  Type the command ```docker-compose up``` 
9.  Wait till you see Airflow Written Boldly in your cmd window.
10. Open any web browser and type this address: ```localhost:8080``` If you get a response such as page not 
    found, just wait for a few seconds and try it again. It will show up.  
11. Trigger the DAG.
12. After a few minutes run a select * query on the jokes_data table and you will see it has been 
    populated with more rows of data. This population process will be done every 2 minutes until the DAG is 
    stopped.
13. Once you've seen this in action and want to stop the process, you can open another cmd window and navigate 
    the directory of your cloned repo just like in step 7.
14. Once you're there, type docker-compose down.
15. After, open Docker, select the containers tab, stop any running containers, and close Docker. 
16. You can close PostgreSQL as well once you're done, to free up PC resources.

**Thank You** 




