# Best invoice AWS Lambda Deployment

At first, you have to build the Docker image, make the platform Linux/amd64 as AWS infra is.

Inside the project directory, run this command  

```bash
 docker buildx build --platform linux/amd64 --provenance=false -t bestinvoice:prod .
```

if you want to test it locally (optional). You have to install the Lambda interface  for Linux

```bash
mkdir -p ~/.aws-lambda-rie && \
    curl -Lo ~/.aws-lambda-rie/aws-lambda-rie https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie && \
    chmod +x ~/.aws-lambda-rie/aws-lambda-rie
```

on Windows 

```bash
$dirPath = "$HOME\.aws-lambda-rie"
if (-not (Test-Path $dirPath)) {
    New-Item -Path $dirPath -ItemType Directory
}
      
$downloadLink = "https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie"
$destinationPath = "$HOME\.aws-lambda-rie\aws-lambda-rie"
Invoke-WebRequest -Uri $downloadLink -OutFile $destinationPath
```

Then start the Docker container, please make sure that you pass the DB creds as -e

```bash
docker run --platform linux/amd64  -v ~/.aws-lambda-rie:/aws-lambda -p 9000:8080 -e DB_HOST="your endpoint" -e DB_PORT=3306 -e MYSQL_USER="user" -e MYSQL_PASSWORD='**********' -e MYSQL_DATABASE=DB-Name \
    --entrypoint /aws-lambda/aws-lambda-rie \
    bestinvoice:prod \
        /usr/local/bin/python -m awslambdaric lambda_handler.lambda_handler

```

to test it 

```bash
curl -XPOST "localhost:9000" \
  -d '{
        "user_id": 91,
        "user_location_id": 7,                                     
        "user_credit_mode": 0,               
        "item_list": [
            {"2": 10},                                                     
            {"3": 5},
            {"4": 20},
            {"5": 1}
        ]
    }' \
  -H "Content-Type: application/json"
```

After that, you have to tag your image as ID.dkr.ecr.region

```bash
docker tag bestinvoice:prod 807124275818.dkr.ecr.eu-central-1.amazonaws.com/best-invoice:latest
```

then you have to login to ecr 

```bash
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 807124275818.dkr.ecr.eu-central-1.amazonaws.com
```

Then you have to push it to AWS ECR

```bash
docker push 807124275818.dkr.ecr.eu-central-1.amazonaws.com/best-invoice:latest  
```