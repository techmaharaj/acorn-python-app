# Acorn Python App

This repo has sample code that shows how to deploy a Python app on Acorn. This is an expense tracker application built using Python and Flask. It uses MongoDB Atlas  as the datastore which is deployed as an Acorn service.

## How to use this repo

### Step 1 - Only UI

We'll first start by deploying only the UI. Navigate to `Step 1 - Only UI` folder and run `acorn run -n expense-app .` this will refer to the Acornfile and deploy the application only with the UI.

Note: To run it in developer mode `acorn dev -n expense-app .`. This will allow you to develop on the fly, meaning any changes that you do, Acorn will watch for it and redeploy the application.

## Deploy MongoDB Atlas as an Acorn Service

We'll be using MongoDB Atlas as a datastore for this example which will be deployed as an Acorn service. Refer to the readme in the `MongoDB-Atlas-Service` folder to deploy MongoDB Atlas a service.

### Step 2 - With Database

After you've understood how Acorn works by deploying only the UI, you can navigate to the `Step 2 - With Database` folder, update the `collection` and `cluster` name in the Acornfile and run `acorn run -n expense-app .` to deploy the application. This time we also have the MongoDB Atlas service deployed along with our code.

Note: If you've enabled the developer mode, you can simply update the code/files and Acorn should update the deployment for you.
