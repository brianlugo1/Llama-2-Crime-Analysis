# Llama-2-Crime-Analysis



The purpose of this project is to run a local instance of Llama2
and feed the instance data about Crime. The end goal is to then
ask the local instance of Llama2 questions about what data or
correlations were found with the Crime data.



Link for supported Models in the Ollama Library:
https://ollama.ai/library



Follow these steps for getting started:

Step 1:
Download Ollama at the following link:
https://ollama.ai/download

Step 2:
After installing Ollama run the command in a terminal:
`ollama run llama2`

While running Ollama, you can ask any question.

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

Run the command to view running containers in Docker:
`docker ps`

Step 4:
Run the command to start a Docker Image of Ollama CPU only:
`docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama`

Step 5:
Run the command to run a Llama2 Model in the running Docker Container:
`docker exec -it ollama ollama run llama2`

Like before, you can ask Llama2 any questions.