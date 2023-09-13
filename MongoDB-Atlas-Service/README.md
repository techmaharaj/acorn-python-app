# Creating MongoDB Atlas Acorn Service

The steps mentioned here are a modification of what is mentioned in [this blog post](https://www.acorn.io/creating-an-acorn-service-for-mongodb-atlas/). We have a `fetchDetails.sh` shell script that basically uses the MongoDB CLI to communicate with your existing MongoDB Atlas account and gets the cluster from the current project.

_Note: Follow these steps, if you already have a MongoDB Atlas account with a cluster, collection and user created._

- Generate the `public_key` and `private_key` keys for your MongoDB Atlas account.
- Note down the `ProjectId` of the current project along with your `cluster` and `collection` name.
- Create a user with Admin access (_if you have not already_) using simple credentials and note down their credentials.
- Update the `username`, `password`, `public_key`, `private_key`, and `project_id` in the Acornfile in this folder.

Once done simply run the following commands to push the image to docker to use this as an Acorn service. *Replace the username with your actual username.*

```sh
acorn build -t docker.io/<username>/acorn-mongo-atlas-service:latest . 
acorn push docker.io/<username>/acorn-mongo-atlas-service:latest
```

With this MongoDB Atlas is successfully deployed as a docker image. We can use that image for your Atlas service.