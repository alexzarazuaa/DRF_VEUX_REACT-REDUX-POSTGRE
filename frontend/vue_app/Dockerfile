FROM node:10-alpine
RUN mkdir /frontend
WORKDIR /frontend
COPY package*.json ./
RUN npm install
COPY . ./
RUN npm run build