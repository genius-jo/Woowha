FROM node:15.5-alpine

# Create app directory
RUN mkdir -p /app/src
WORKDIR /app

# `/app/node_modules/.bin`을 $PATH 에 추가
# ENV PATH /app/node_modules/.bin:$PATH

# app dependencies, install 및 caching
COPY package.json ./
RUN npm install
RUN npm install -g react-scripts
RUN npm install -g react-router-dom

# 소스 복사
COPY . .

# 앱 실행
CMD ["npm", "start"]