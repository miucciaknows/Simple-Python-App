# Simple Python App
 This simple application just calculates the sum of two numbers through the value of two numbers sent in a request by the user. 
 
 The purpose is to use this application as an example of teaching how to create custom extensions on IBM's **Watsonx Assistant**.

## Article available with instructions for use on medium through the link

[https://medium.com/@nathalia.trazzi/getting-started-with-watsonx-assistant-iv-3c7aadb9e598](https://medium.com/@nathalia.trazzi/getting-started-with-watsonx-assistant-ii-b434486470bd)

## Running the application


To make a request to this application, simply pass the following request (in JSON format)

`

{
	"number1": 10,
	"number2": 20
}
`
#### Using locally 

Open your terminal and type the following command:

`git clone https://github.com/miucciaknows/Simple-Python-App.git`

Open your favorite terminal and install the libraries used in this project

-> But first make sure you are in the correct directory path.

`cd sum/source/rest_api`

And then:

`pip3 install requirements.txt`

or, depending on the version of Python used on your machine.

`pip install requirements`

Now, you can run the code with:

`python3 main.py`

or, depending on the version of Python used on your machine.

`python main.py`

To make the request, You can use Insomia or any other software of your choice.

![Image 1](./Images/01.png)

### Using through Docker
