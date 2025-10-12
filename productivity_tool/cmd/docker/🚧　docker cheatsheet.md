---
created_at: 2025/07/13 17:38:39
updated_at: 2025/07/24 00:17:53
---
```
$ docker version
```

```
# <CONTAINER> = <CONTAINER_ID> or <CONTAINER_NAME>

$ docker container ls --all
$ docker container ls --quiet

$ docker container rm $(docker container ls --all --quiet)
$ docker container rm --force $(docker container ls --quiet)

$ docker container top <CONTAINER>

$ docker container logs <CONTAINER>

$ docker container inspect <CONTAINER>
$ docker container inspect --format ...
$ docker container inspect --format='{{.LogPath}}' ...

$ docker container stats <CONTAINER>

$ docker container run --interactive --tty ...
$ docker container run --detach --publish 8080:80 ...
$ docker container run --env <KEY>=<VAL> ...
$ docker container run --restart ...
$ docker container run --mount type=bind,source=<HOST_DIR>,target=<CONTAINER_DIR>
$ docker container run --detach --log-driver=fluentd ...

$ docker container port <CONTAINER>
```

```
# <IMAGE> = <IMAGE_NAME>

$ docker image ls --all
$ docker image ls --quiet
$ docker image ls "<PATTERN>"

$ docker image rm $(docker image ls --all --quiet)

$ docker image build --tag <IMAGE> .

$ docker image history <IMAGE>

$ docker image tag <IMAGE> <REGISTRY>/<ORG>/<REPOSITORY>:<TAG>

$ docker image push <REGISTRY>/<ORG>/<REPOSITORY>:<TAG>
```

```
$ docker network create ...
$ docker network create --driver overlay ...
```

```
# <VOLUME> = <VOLUME_NAME>

$ docker volume ls
$ docker volume create <VOLUME>
$ docker volume rm <VOLUME>
$ docker volume prune
```

```
$ docker system df
$ docker system prune
```

```
$ docker manifest inspect <IMAGE>
```

```
$ docker buildx ls
$ docker buildx inspect ...
$ docker buildx build ...
```

```
$ docker-compose version
$ docker-compose up
$ docker-compose down
$ docker-compose start
$ docker-compose stop
$ docker-compose -f <FILE_1> -f <cd FILE_2> config
```

```
$ cat ~/.docker/config.json
```

```
$ cat ~/.docker/daemon.json
{
	"insecure-registries": ["..."],
	"metrics-addr": "...",
	"experimental": "..."
}
```

```
$ docker swarm init
$ docker swarm init --force-new-cluster
$ docker swarm join-token worker
$ docker swarm join-token manager
$ docker swarm leave --force

$ docker node ls
$ docker node update --label-add <KEY>=<VAL ...
$ docker node update --availability drain ...
$ docker node update --availability active ...
$ docker node promote ...
$ docker node demote ...

$ docker service ls
$ docker service ps ...
$ docker service logs ...
$ docker service inspect ...
$ docker service update ...
$ docker service update --rollback ...

$ docker stack deploy ...
$ docker stack services ...
$ docker stack ps ...
$ docker stack rm ...

$ docker config create ...
$ docker config ls
$ docker config inspect ...

$ docker secret create ...
$ docker secret inspect --pretty ...

$ docker context create ...
$ docker context ls ...
$ docker context inspect ...
$ docker context use ...
```
