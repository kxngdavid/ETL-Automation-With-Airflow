ETL pipeline Automation With Airflow
---

This project focuses on automating a workflow. The workflow fetches semi-structured data from an API
every two (2) minutes, transforms it into a structured format, and dumps the data into a PostgreSQL database.




## Prerequisites
- Docker
- PostgreSQL





## Getting Started

Following these instructions will get the project up and running on your local machine for learning, testing, and development purposes

-  Clone the repository.

-  Open Docker and make sure the Docker engine is running. 

-  Open PostgreSQL and be sure it's up and running.

-  Open the **"postgres_db_credentials.txt"** file in the repository and set your PostgreSQL database credentials.

-  Navigate through the Airflow folder into the dags folder. Locate the "db_config_airflow.txt" file and set 
    the credentials for the PostgreSQL database. NB: For this specific file, please bear in mind that this is what your localhost
    should be set to : ```host.docker.internal```

-  Open and run the ```etl_pipeline.py``` file.


## Usage

-  After executing the ```etl_pipeline.py``` file above, check your Postgres database to be sure a table named ```jokes_data``` has been created
    and populated with 10 rows of data from the API.
 	
-  Open up your cmd/terminal and navigate to the cloned repository. Make sure you are inside the repository at
    the first level. eg: ```C:\Program Files\GitHub\ETL-Automation-With-Airflow>```		
 
-  Type the command ```docker-compose up``` 

-  Wait till you see Airflow Written Boldly in your cmd window.

- Open any web browser and check http://localhost:8080/   

- Trigger the DAG.

- After a few minutes run a ```select *``` query on the jokes_data table and you will see it has been 
    populated with more rows of data. This population process will be done every 2 minutes until the DAG is 
    stopped.


## Closing the Project

- To stop the process in a safe way, you can open another cmd window and navigate 
    the directory of your cloned repo just like in step 7.

- Once you're there, type docker-compose down.

- After, open Docker, select the containers tab, stop any running containers, and close Docker. 

- You can close PostgreSQL as well once you're done, to free up PC resources.


## Credits

- [Apache Airflow](https://github.com/apache/incubator-airflow)
- [docker-airflow](https://github.com/puckel/docker-airflow/tree/1.10.0-5)




