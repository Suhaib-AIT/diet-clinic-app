FROM node:20-alpine
WORKDIR /app
COPY package.json tsconfig.json vite.config.ts ./
COPY src ./src
COPY public ./public
RUN npm install && npm run build
CMD ["npm", "run", "preview", "--", "--host"]
