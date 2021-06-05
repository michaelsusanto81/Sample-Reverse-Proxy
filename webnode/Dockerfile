FROM node:14-slim

# Create webnode directory
RUN mkdir /webnode

# Install webnode dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json /webnode/package*.json

WORKDIR /webnode

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

# Bundle webnode source
COPY . /webnode