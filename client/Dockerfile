FROM node:18-alpine

WORKDIR /usr/src/app

COPY package.json yarn.lock ./

RUN yarn install

COPY . .

RUN yarn build

EXPOSE 80

CMD ["yarn", "vite", "preview", "--host", "0.0.0.0", "--port", "80"]