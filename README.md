# Llama-2-Crime-Analysis



The purpose of this project is to run a local instance of Llama2
and feed the instance data about Crime. The end goal is to then
ask the local instance of Llama2 questions about what data or
correlations were found with the Crime data.



Link for supported Models in the Ollama Library:
https://ollama.ai/library

Link for Ollama and Docker Tutorial:
https://collabnix.com/getting-started-with-ollama-and-docker/

Link for running Ollama locally:
https://medium.com/mad-chatter-tea-party/how-to-run-a-local-model-with-ollama-99cd98665760

Link for fine-tuning Llama2:
https://www.datacamp.com/tutorial/fine-tuning-llama-2

Link for youtube tutorial for fine-tunning Llama2 model:
https://www.youtube.com/watch?v=3fsn19OI_C8

Another link for youtube tutorial for fine-tunning:a
https://www.youtube.com/watch?v=MDA3LUKNl1E

Link to Huggingface Documentation for Llama2:
https://huggingface.co/docs/transformers/main/model_doc/llama2



Follow these steps for getting started:
Step 1:
Download Ollama at the following link:
https://ollama.ai/download

To install Ollama on linux run:
`curl -fsSL https://ollama.com/install.sh | sh`

If you get the following message when running the above command:
`Warning: Failed to open the file /tmp/tmp.NagPY7b0uu/ollama: No such file or`
`Warning: directory 0.0%curl: (23) Failure writing output to destination`

Run the commands:
`sudo snap remove curl`
`sudo apt install curl`

Run the command to reboot linux system for installing NVIDIA CRUD drivers:
`reboot`

Llama2 7B Model is pulled by default.

To pull Llama2 13B Model run:
`ollama pull llama2:13b`

To pull Llama2 70B Model run:
`ollama pull llama2:70b`

To pull any model you want from the library run:
`ollama pull [model_name]`

To pull any model and corresponding size run:
`ollama pull [model_name]:[model_size]`

NOTE:

At least 8GB of RAM is suggested for 7B Models.
At least 16GB of RAM is needed for 13B Models.
At least 32GB of RAM is needed for 70B Models.

Step 2:
After installing Ollama run the command in a terminal:
`ollama run llama2`

To run any model run:
`ollama run [model_name]`

To run any model and corresponding size run:
`ollama run [model_name]:[model_size]`

To list stored models run the command:
`ollama list`

While running Ollama, you can ask your model any question you want!

To save your session:
`/save <model_name>`

To load a saved session:
`/load <model_name>`

To exit:
`/bye`

For help:
`/?`

Step 3:
Download Docker at the following link:
https://docs.docker.com/desktop/

Run the following command to ensure you have installed Docker correctly:
`docker`

If the command is not recognized, you have not installed Docker correctly.

Here is a link for Troubleshooting Docker issues:
https://www.digitalocean.com/community/tutorials/how-to-debug-and-fix-common-docker-issues

Ensure that you have Docker running before moving on past this point.

To view running containers in Docker run:
`docker ps`

If you get the following error message in Linux when running the command `docker ps`:
`permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json": dial unix /var/run/docker.sock: connect: permission denied`

Run the following command:
`sudo chmod 666 /var/run/docker.sock`

Step 4:
Run the command to create and start a Docker Image of Ollama CPU only:
`docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama`

To stop the running ollama container run:
`docker stop ollama`

To stop any running container in Docker run:
`docker stop [container_name]`

To restart the already created but stopped Docker Container run:
`docker start ollama`

To restart any existing Docker Container run:
`docker start [container_name]`

To rename an existing Docker Container run:
`docker rename [old_container_name] [new_container_name]`

Step 5:
Run the command to run a Llama2 Model in the running Docker Container:
`docker exec -it ollama ollama run llama2`

To run any model and size in any running Docker Container run:
`docker exec -it [container_name] ollama run [model_name]:[model_size]`

Step 6:
Follow the instructions for downloading postgres:
https://postgresapp.com/downloads.html

To install PostgreSQL in linux run:
`sudo apt install postgresql`

To use the operating system user postgres type the command:
`sudo -u postgres -i`

Follow the instructions for setting up postgres:

Step 1:
To check if you correctly installed postgres, open a new terminal session.

Run the command `psql`.

If you get a message saying command not found, you have not correctly
installed postgress. You will not be able to continue with the
instructions until you correctly install postgres.

Go to the link for help on troubleshooting:
https://postgresapp.com/documentation/troubleshooting.html

Step 2:
Run the command `createdb crime` to create the new database in postgresql.

Step 3:
Run the command `psql crime` to open a connection to the database.

Step 4:
Run the command `\q` to quit session.

To dump the PostgreSQL openai db:
Run `pg_dump crime >> file_name.sql`

Follow these steps for running the project:

Step 1:
Ensure that you have python installed!

Here is a link for installing python:
https://www.python.org/downloads/

NOTE:
For MacOS/Linux use:
`python3` and `pip3`

Windows use:
`python` and `pip`

Step 2:
Open a terminal.

Step 3:
Run the command:
`pip3 install -r requirements.txt`

Step 4:
Run the command:
`python3 llama.py`

Step 5:
Ask your local instance of Llama2 a question!

Waiting for a response from your local instance of Llama2 will take
longer depending on your machine's computing power.

Type `exit` to terminate the program!