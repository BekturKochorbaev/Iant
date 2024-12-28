# Используем официальный образ Nginx
FROM nginx:stable-alpine

# Устанавливаем рабочую директорию
WORKDIR /etc/nginx

# Копируем файл конфигурации Nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf

# Указываем порт, на котором Nginx будет слушать
EXPOSE 80

# Запускаем Nginx
CMD ["nginx", "-g", "daemon off;"]