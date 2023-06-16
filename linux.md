## Linux tricks

#### BLAS/LAPACK on Debian/Ubuntu

BLAS:
```bash
$ sudo update-alternatives --config libblas.so.3
```

LAPACK:
```bash
$ sudo update-alternatives --config liblapack.so.3
```
On ubuntu one must use openblas with standard lapack for numpy to work.

to install openblas
```bash
$ sudo apt-get install libopenblas-base
```

Note that the number of threads used by openblas can be set manually by:
```bash
$ export OPENBLAS_NUM_THREADS=1
```


#### Install certificate for ssh connexion

In order to allow certificate based connexion to a ssh server

```bash
$ ssh-copy-id -i ~/.ssh/id_rsa.pub login@server
```

#### .ssh/confif file

Simple examples for ssh config file

```
Host github.com
  Hostname ssh.github.com
  Port 443
Host other_pc
  Hostname 192.168.0.something
  User username 
Host cproxy
  Hostame 192.168.0.something
  User username
  ProxyCommand ssh user@proxy-server.example.com -W %h:%p
Host cproxy_other
  Hostame 192.168.0.something
  ProxyJump other_pc
```


#### Amazon aws

Copy all file in a folder to an aws s3 folder
```bash
$ ls * |xargs -n 1 -I {} aws s3 cp {} "s3://URL" 
```


#### Convert images to mp4 movie

```bash
$ convert -delay 20 *.png movie.mp4
```

#### Disable autofocus opn webcam

```bash
$ v4l2-ctl --set-ctrl=focus_auto=0
```

#### Get SSL let's encrypt certificate

Think about descativating nginx so that the temporary server works and install the wawesome certbot

```bash
$ sudo certbot certonly --rsa-key-size 2048 --standalone --agree-tos --no-eff-email --email your@email.com -d your.server.com

```

keys will be stored for use in apache/nginx in /etc/letsencrypt/live/your.server.com/fullchain.pem



