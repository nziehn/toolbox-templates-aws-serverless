# tb-aws-lambda-base

This is a basic project for deploying clean python-based serverless applications.






## install

1. make sure you have serverless running locally
1. install pip:
    ```shell script
    pip install -r requirements.txt
    ``` 

## running locally

1. Scripts can be run directly, as long as PYTHONPATH includes the root directory of the repo
1. Run it through serverless invoke:
    ```shell script
    serverless invoke local --function example --stage=local
    ```  
   

## deployment

1. If you want to interact with a VPC, you should run it as a regional lambda
    - Regional lambdas need a NAT gateway to access the internet
    
2. Use the following command to deploy:
    ```
    SLS_DEBUG=* sls deploy --stage "${BRANCH_NAME}" --git-commit $(git log --pretty=format:'%h' -n 1)
   ```
   
  