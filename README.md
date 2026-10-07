# Python Flask Application Deployment with Nginx on AWS EC2

A simple DevOps practical demonstrating how to deploy a Python Flask web application on an AWS EC2 Ubuntu server using Nginx as a reverse proxy.

## Architecture

                    Internet
                       |
                       | HTTP :80
                       v
                +-------------+
                |   AWS EC2   |
                |   Ubuntu    |
                +-------------+
                       |
                       v
                +-------------+
                |    Nginx    |
                |    :80      |
                +-------------+
                       |
                       | Proxy
                       v
                +-------------+
                | Flask App   |
                |   :5000     |
                +-------------+
                       |
                       v
                LoveConnect
                Welcome Page


## Technologies Used

* AWS EC2
* Ubuntu Linux
* Python
* Flask
* Nginx
* Git
* GitHub
* AWS Security Groups

## Application

The project contains a simple dating application landing page called **LoveConnect**.

The Flask application runs internally on:


127.0.0.1:5000


Nginx listens on:

0.0.0.0:80


Nginx forwards incoming HTTP requests to the Flask application.

## Prerequisites

* AWS account
* Ubuntu EC2 instance
* SSH access to the EC2 instance
* Python 3
* Git

## Step 1: Launch EC2

Create an Ubuntu EC2 instance.

Configure the Security Group with:

| Protocol | Port | Source    |
| -------- | ---: | --------- |
| SSH      |   22 | Your IP   |
| HTTP     |   80 | 0.0.0.0/0 |

SSH into the instance:

ssh -i "your-key.pem" ubuntu@YOUR-EC2-PUBLIC-IP

## Step 2: Update Ubuntu

sudo apt update

## Step 3: Install Python and Flask

sudo apt install python3 python3-pip python3-flask -y

Verify:

python3 --version
flask --version

## Step 4: Clone the Repository

git clone https://github.com/YOUR-USERNAME/flask-nginx-ec2-deployment.git

Move into the project:

cd flask-nginx-ec2-deployment

## Step 5: Test Flask Application

Run:

python3 app.py

The application will start on:

127.0.0.1:5000

From another SSH session, test:

curl http://127.0.0.1:5000

You should receive the HTML response from the Flask application.

## Step 6: Install Nginx

sudo apt install nginx -y

Check the service:

sudo systemctl status nginx

Test the configuration:

sudo nginx -t


## Step 7: Configure Nginx Reverse Proxy

Create the configuration:

sudo nano /etc/nginx/sites-available/dating-app


Add:

nginx
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:5000;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}


Enable the configuration:

sudo ln -s /etc/nginx/sites-available/dating-app /etc/nginx/sites-enabled/

Remove the default Nginx configuration:

sudo rm -f /etc/nginx/sites-enabled/default

Test:

sudo nginx -t

Restart Nginx:

sudo systemctl restart nginx


## Step 8: Verify Nginx

Check that Nginx is listening on port 80:

sudo ss -lntp | grep :80

Test locally:

curl http://localhost

## Step 9: Access the Application

Open the EC2 public IP in a browser:

http://YOUR-EC2-PUBLIC-IP

The LoveConnect welcome page should be displayed.

## Troubleshooting

### Nginx is not running

sudo systemctl status nginx

Start it:

sudo systemctl start nginx

Enable it at boot:

sudo systemctl enable nginx

### Nginx configuration error

sudo nginx -t

Check logs:

sudo tail -f /var/log/nginx/error.log

### Flask is not running

Check:

curl http://127.0.0.1:5000

Start the application:

python3 app.py

### Browser shows `ERR_CONNECTION_TIMED_OUT`

Check the AWS Security Group and make sure TCP port 80 is allowed.

Also check:

sudo ss -lntp | grep :80

If UFW is enabled:

sudo ufw status
sudo ufw allow 80/tcp

## Request Flow

When a user opens:

http://EC2-PUBLIC-IP

the request follows:

Browser
   |
   | HTTP :80
   v
AWS Security Group
   |
   v
Nginx
   |
   | proxy_pass
   v
Flask :5000
   |
   v
LoveConnect HTML

## DevOps Concepts Demonstrated

* AWS EC2 provisioning
* Linux server administration
* SSH
* AWS Security Groups
* Python application deployment
* Flask
* Nginx reverse proxy
* Port management
* Linux service management
* Application troubleshooting
* Git and GitHub

## Future Improvements

* Run Flask using Gunicorn
* Create a systemd service
* Add HTTPS using Let's Encrypt
* Add CI/CD using Jenkins or GitHub Actions
* Containerize the application using Docker
* Deploy the application to Kubernetes
* Add Prometheus and Grafana monitoring

## Author

**Kashim Basaragi**

Infrastructure & DevOps Engineer

Skills demonstrated: AWS, Linux, Python, Flask, Nginx, Git, GitHub and DevOps.
