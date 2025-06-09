<pre>POST /login
payload: {
    "login": "MyNickName",
    "password": "MyPassword"
}
-> {"result": bool}


POST /users/new 
payload: {
    "admin_name": "admin",
    "admin_password": "dsfdskjdfjdsfjdsf",
    "data": {
        "login": "MyNickName",
        "name": "Ivan",
        "password": "MyPassword",
        "surname": "Ivanov"
    }
}
-> {"result": bool}

/* TODO */
POST /user/delete
payload: {
    "admin_name": "kdsofijdsofijdsfoij",
    "admin_password": "dsfdskjdfjdsfjdsf",
    "data": {
        "login": "MyNickName"
    }
}
-> {"result": bool}

POST /add/tg
payload: {
    "admin_name": "kdsofijdsofijdsfoij",
    "admin_password": "dsfdskjdfjdsfjdsf",
    "data": {
        "author": "Ivan Petrov",
        "source": "DailyMail",
        "date": 1749323479,
        "header": "John Doe Runs Every Day",
        "text": "mhm first of alll blah blah"
    }
}
-> {"result": bool}

POST /add/web
payload: {
    "admin_name": "kdsofijdsofijdsfoij",
    "admin_password": "dsfdskjdfjdsfjdsf",
    "data": {
        "source": "DailyMail",
        "author": "Ivan Petrov",
        "date": 1749323479,
        "header": "John Doe Runs Every Day",
        "text": "mhm first of alll blah blah",
        "links": [
            "https://ohno.bruh/lmao",
            "https://kek.elite?today=never"
        ]
    }
}
-> {"result": bool}</pre>
