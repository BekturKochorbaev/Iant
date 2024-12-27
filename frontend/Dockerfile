# Используем официальный образ Node.js
FROM node:18-alpine AS builder

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json для установки зависимостей
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем весь исходный код
COPY . .

# Сборка TypeScript в JavaScript
RUN npm run build

# Production Stage: минимальный образ для выполнения приложения
FROM node:18-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости из builder
COPY --from=builder /app/node_modules ./node_modules

# Копируем собранное приложение
COPY --from=builder /app/dist ./dist

# Указываем порт, на котором работает приложение
EXPOSE 3000

# Команда запуска приложения
CMD ["node", "dist/main"]
