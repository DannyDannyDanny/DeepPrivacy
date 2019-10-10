# DeepPrivacy
# [Link to KanBan](https://github.com/DannyDannyDanny/DeepPrivacy/projects/1?fullscreen=true)

## Run App

Run locally
`python app.py`

View logs in real time
```bash
docker-compose logs -f
```

Submit request to WSGI
```bash
# run locally - note the return link has remote machine IP harcoded
$ curl -F "file=@lady.png" localhost:5000/
{"file_url":"./public/1640b1a4-35e7-43dc-9366-ecf8f623e734.png"}

# run locally
$ curl -F "file=@lady.png" localhost:5000/
{"file_url":"./public/1640b1a4-35e7-43dc-9366-ecf8f623e734.png"}
```

Manually Sync src from local to server
```bash
# move files from local to offsite repo
$ git pull
# if there are any huge files use:
$ rsync -avz DeepPrivacy/ root@142.93.98.12:/home/DannyDannyDanny/DeepPrivacy
```

Rebuild application after src changes
```bash
# once copied run inside DeepPrivacy
docker-compose up --build -d
```
