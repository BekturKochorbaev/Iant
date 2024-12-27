# Используем официальный образ Nginx
FROM nginx:stable-alpine

# Устанавливаем рабочую директорию
WORKDIR /etc/nginx

# Копируем файл конфигурации Nginx (создайте свой nginx.conf)
COPY nginx.conf /etc/nginx/nginx.conf

# Копируем статические файлы, если это фронтенд (например, React, Next.js)
# Убедитесь, что вы изменили путь на папку с вашим build
COPY ./dist /usr/share/nginx/html

# Указываем порт, на котором Nginx будет слушать
EXPOSE 80

# Запускаем Nginx
CMD ["nginx", "-g", "daemon off;"]
