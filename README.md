# Connector-Python
Uses a CentOS 7 base image to deploy a container with MariaDB Connector/Python installed and ready to use.

# Dependencies

* [Docker Engine](https://docs.docker.com/engine/install/)
* [`docker-compose`](https://docs.docker.com/compose/install/)

# Install and Run
Open a terminal with `docker-compose` installed, change directory into where you downloaded/extracted the code, then run-

```
docker-compose up;
```

# Run your Code
Add your Python code files to the `my_python_code` directory. These will appear at `/root/my_python_code/` in the container. Note the repository comes with `test.py` by default.

Get a shell to the container with-

```
docker exec -it connector-python bash
```

You can then run your Python code like-

```
python3 /root/my_python_code/test.py
```

Where `/root/my_python_code/test.py` is replaced with the path to your Python code file.

# Connecting to MariaDB
The container only provides connector infrastructure, it does not provide a running MariaDB server. Reference [Connector/Python documentation](https://mariadb.com/docs/appdev/connector-python/#opening-a-connection) to learn how to specify parameters to open a connection to a remote MariaDB server.
