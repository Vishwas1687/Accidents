FROM node:20.11.0

# Install frontend dependencies and build the React app
WORKDIR /frontend
COPY ./package*.json ./
RUN npm install --force
COPY . .

# Expose the necessary port
EXPOSE 3000

CMD ["npm", "start"]