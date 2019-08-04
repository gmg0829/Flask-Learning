docker build -t flask:0.1 .

docker run --name flask_app -v $PWD/app:/app -p 5000:5000 flask:0.1

目前主流的部署方案是 nginx + uwsgi，下面我们将介绍如何为生产环境部署web应用程序。Nginx是一个开源web服务器，uWSGI是一个快速、自我修复、开发人员和系统管理员友好的服务器。

docker run -it --name flaskapp -p 5000:5000 -v $PWD/app:/app docker-flask:0.1 -d debug

