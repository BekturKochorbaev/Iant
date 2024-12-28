# Используем официальный образ Node.js
FROM node:18-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json для установки зависимостей
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем весь исходный код
COPY . .

# Сборка Next.js приложения
RUN npm run build

# Production Stage: минимальный образ для выполнения приложения
FROM node:18-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json
COPY --from=builder /app/package*.json ./

# Устанавливаем только production зависимости
RUN npm install --production

# Копируем необходимые файлы для Next.js
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public

# Указываем порт, на котором работает приложение
EXPOSE 3000

# Команда запуска приложения
CMD ["npm", "start"]