# Используем официальный образ Node.js
FROM node:18-alpine AS builder

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json
COPY Country/frontend/package*.json ./

# Устанавливаем зависимости
RUN npm ci

# Копируем весь проект
COPY Country/frontend/ .

# Собираем проект
RUN npm run build

# Финальный образ
FROM node:18-alpine AS runner

WORKDIR /app

# Копируем собранный проект и зависимости
COPY --from=builder /app/next.config.js ./
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

# Expose порт
EXPOSE 3000

# Команда для запуска
CMD ["npm", "start"]