## build docker

```docker build -t story_maker .```

## run docker

```docker run -d -p 8051:8051 --name story_maker_api story_maker```

command above will run the API at [port 8051](http://127.0.0.1:8051)

## API docs

### URL:
if run in your localhost
`http://localhost:8051/createstory`

### header:

`Content-Type:application/json`

`openai_key:<youropenaiapikey>`

### body:

`"age":4`

`"gender": "laki-laki"`

`"specific_topic": "perjalanan ke luar angkasa"`

`"n_sentence": 20`
