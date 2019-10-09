# DeepPrivacy
# [Link to KanBan](https://github.com/DannyDannyDanny/DeepPrivacy/projects/1?fullscreen=true)

## Run App
`FLASK_APP=app.py python -m flask run`

`python app.py`


```bash
$ curl -F "file=@lady.png" localhost:5000/
{"file_url":"./public/1640b1a4-35e7-43dc-9366-ecf8f623e734.png"}
```

```bash
# move files from local to offsite repo
$ rsync -avz DeepPrivacy/ root@142.93.98.12:/home/DannyDannyDanny/
```

```bash
# once copied run inside DeepPrivacy
docker-compose up --build -d
```
