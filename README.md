# Acorn Python App

This repo has sample code that shows how to deploy a Python app on Acorn. This is an expense tracker application built using Python and Flask. It used PostgreSQL as the datastore.

## How to use this repo

### Step 1 - Only UI

We'll first start by deploying only the UI. Navigate to `Step 1 - Only UI` folder and run `acorn run -n expense-app .` this will refer to the Acornfile and deploy the application only with the UI.

Note: To run it in developer mode `acorn dev -n expense-app .`. This will allow you to develop on the fly, meaning any changes that you do, Acorn will watch for it and redeploy the application.

### Step 2 - With Database

After you've understood how Acorn works by deploying only the UI, you can navigate to the `Step 2 - With Database` folder and run `acorn run -n expense-app .` to deploy the application. This tieme we also have a PostgreSQL container and our code now stores the expense data in the table.

Note: If you've enabled the developer mode, you can simply update the code/files and Acorn should update the deployment for you. 