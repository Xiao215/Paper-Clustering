# Paper-Clustering

###### This project is inspired by the article [What’s Trending in AI — Topic Modeling of AI Papers in 2022](https://txt.cohere.ai/topic-modeling-trending-ai-papers/) from co:here AI.

The backend is implemented on `Flask` for the purpose of a REST API.

## Set up

1. Initialize a virtual environment called `venv` with `virtualenv`.

```
virtualenv venv
```

2. Install all the required packages

```
pip3 install -r requirements.txt
```

3. Create an environment file, `.env`, and store the co:here api key inside in the format of

```
# inside .env
COHERE_API_KEY = YOUR_KEY
```

4. Run the server

```
flask run
```
