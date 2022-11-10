# Представление для авторизации
from flask import request
from flask_restx import Resource, Namespace, abort

from implemented import user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthRegisterView(Resource):
    """
    Класс регистрации
    """
    def post(self):
        """
        Создание пользователя
        """
        req_json = request.json
        email = req_json.get('email')
        password = req_json.get('password')
        if not email and not password:
            abort(400)

        user_service.create(req_json)
        return "Пользователь создан", 201


@auth_ns.route('/login/')
class AuthLoginView(Resource):
    """
    Класс аутентификации
    """
    def post(self):
        """
         Получение токенов при успешной проверке логина и пароля
        """
        req_json = request.json
        email = req_json.get('email')
        password = req_json.get('password')
        if not email and not password:
            abort(400)

        return user_service.auth_user(email, password), 201

    def put(self):
        """
        Обновление refresh токена
        """
        req_json = request.json
        refresh_token = req_json.get('refresh_token')
        if not refresh_token:
            abort(400)

        return user_service.check_token(refresh_token), 201
