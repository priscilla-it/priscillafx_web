# Node Install
FROM node:alpine as build

# Copy package.json and yarn.lock
COPY package.json yarn.lock ./

# Install Yarn globally
RUN npm install -g yarn

# Install dependencies using Yarn
RUN yarn install

# Copy the rest of the application code
COPY . .

# Build the application
RUN yarn build

# Nginx Install
FROM nginx:stable-alpine

# Copy the built application and Nginx configuration
COPY --from=build /dist /usr/share/nginx/html
COPY --from=build nginx.conf /etc/nginx/conf.d/default.conf

# Expose API (Next.js local port: 50160)
EXPOSE 50161

# Startup Nginx
CMD ["nginx", "-g", "daemon off;"]

