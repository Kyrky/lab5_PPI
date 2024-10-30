# SAW: Project Requirements for Bug Tracker

## Project Description
This project is a Bug Tracking System (Bug Tracker) designed to help users identify and document software issues. The system allows users to create accounts, submit bug reports, view details of each report, and manage bug statuses.

## Functional Requirements

### 1. User Registration and Authentication
- Users should be able to register a new account by providing a username, email, and password.
- Users log in with an email and password.
- Passwords should be stored in a hashed format for security.

### 2. Bug Report Creation
- An authenticated user can create a new bug report.
- Report fields should include:
  - Title (required)
  - Description (required)
  - Steps to reproduce (optional)
  - Expected result (optional)
  - Actual result (optional)
  - Priority (low, medium, high) (optional)
  - Assigned to (optional)
  - Status (open, in progress, resolved) (optional)

### 3. Viewing Reports
- Users can view all their created reports on the "Dashboard" page.
- Each report should show a brief overview, including title, creation date, and status.
- Users can click on a report to view detailed information.

### 4. Viewing Report Details
- When viewing report details, users should see all information related to the bug, including title, creation date, description, reproduction steps, expected and actual results, priority, assigned user, and status.

### 5. Managing Bug Status
- Users can update the status of a report (open, in progress, resolved).

### 6. Security
- User passwords should be securely hashed using bcrypt.
- Only authenticated users can access the "Dashboard" and "Create New Report" pages.

## Non-Functional Requirements

### 1. Performance
- Page load time should not exceed 2 seconds.

### 2. UI Design
- The interface should be intuitive and user-friendly.
- Form fields should have placeholders for a better user experience.

### 3. Compatibility
- The system should support modern web browsers (Chrome, Firefox, Edge, Safari).

### 4. Security
- Use secure methods for password storage.
- Protect against brute-force attacks.

### 5. Backup
- Database should be regularly backed up to prevent data loss.

## Technological Requirements
- **Programming Language**: Python 3
- **Framework**: Flask
- **Database**: SQLite for local storage
- **Password Hashing**: Flask-Bcrypt
- **User Authentication**: Flask-Login

## Future Improvements
- Add sorting and filtering options for reports based on priority and status.
- Implement user roles (administrator, tester).
- Add functionality to export reports in PDF or CSV format.
- Migrate to a more scalable database like PostgreSQL or MySQL for larger projects.
- Develop an API for integration with other bug tracking systems.

## File Structure Summary
- **app.py**: Main application file that defines routes and logic.
- **templates/**: Contains HTML templates for various pages (e.g., login, register, dashboard, report view).
- **static/**: Contains static files, including CSS for styling.
- **site.db**: SQLite database file storing user and report data.
- **SAW.md**: Requirements document detailing project specifications.

---

# SAW: Вимоги до проєкту Bug Tracker

## Опис проєкту
Цей проєкт є системою відстеження помилок (Bug Tracker), розробленою для допомоги користувачам у виявленні та документуванні помилок у програмному забезпеченні. Система дозволяє користувачам створювати облікові записи, створювати звіти про помилки, переглядати деталі кожного звіту та керувати статусами помилок.

## Функціональні вимоги

### 1. Реєстрація та авторизація користувача
- Користувач повинен мати можливість зареєструвати новий обліковий запис із зазначенням імені користувача, електронної пошти та пароля.
- Для входу в систему користувач вводить електронну пошту та пароль.
- Паролі повинні зберігатися у хешованому вигляді для забезпечення безпеки.

### 2. Створення звіту про помилку
- Авторизований користувач може створити новий звіт про помилку.
- Поля звіту повинні включати:
  - Назва (обов'язкове)
  - Опис (обов'язкове)
  - Кроки для відтворення (необов'язкове)
  - Очікуваний результат (необов'язкове)
  - Фактичний результат (необов'язкове)
  - Пріоритет (низький, середній, високий) (необов'язкове)
  - Відповідальний (необов'язкове)
  - Статус (відкритий, в процесі, вирішений) (необов'язкове)

### 3. Перегляд звітів
- Користувач може переглядати всі створені ним звіти на сторінці "Dashboard".
- Кожен звіт повинен мати короткий опис, включаючи назву, дату створення та статус.
- Користувач може натиснути на звіт для перегляду детальної інформації.

### 4. Перегляд деталей звіту
- При перегляді деталей звіту користувач повинен бачити всю інформацію, пов'язану з помилкою:
  - Назва, дата створення, опис, кроки для відтворення, очікуваний та фактичний результат, пріоритет, відповідальний та статус.

### 5. Керування статусами помилок
- Користувач може оновлювати статус звіту (відкритий, в процесі, вирішений).

### 6. Безпека
- Паролі користувачів повинні зберігатися у хешованому вигляді за допомогою алгоритму bcrypt.
- Доступ до сторінок "Dashboard" та "Create New Report" дозволений лише для авторизованих користувачів.

## Нефункціональні вимоги

### 1. Продуктивність
- Час завантаження сторінки не повинен перевищувати 2 секунд.

### 2. UI Дизайн
- Інтерфейс повинен бути інтуїтивно зрозумілим і зручним для користувача.
- Поля форм повинні мати підказки для покращення користувацького досвіду.

### 3. Сумісність
- Система повинна підтримувати сучасні веб-браузери (Chrome, Firefox, Edge, Safari).

### 4. Безпека
- Використання захищених методів для зберігання паролів.
- Аутентифікація користувачів повинна бути безпечною та захищати від атак типу brute-force.

### 5. Резервне копіювання
- База даних повинна регулярно зберігатися для запобігання втраті даних.

## Технологічні вимоги
- **Мова програмування**: Python 3
- **Фреймворк**: Flask
- **База даних**: SQLite для локального зберігання
- **Хешування паролів**: Flask-Bcrypt
- **Аутентифікація користувачів**: Flask-Login

## Майбутні поліпшення
- Додавання можливості сортування та фільтрації звітів за пріоритетом та статусом.
- Створення ролей для користувачів (адміністратор, тестувальник).
- Додавання функціональності для експорту звітів у формат PDF або CSV.
- Перехід на більш масштабовану базу даних, таку як PostgreSQL або MySQL, для великих проєктів.
- Розробка API для інтеграції з іншими системами відстеження помилок.

## Короткий опис структури файлів
- **app.py**: Головний файл програми, який визначає маршрути і логіку.
- **templates/**: Містить HTML шаблони для різних сторінок (наприклад, login, register, dashboard, report view).
- **static/**: Містить статичні файли, включаючи CSS для стилізації.
- **site.db**: SQLite файл бази даних, що зберігає дані користувачів і звітів.
- **SAW.md**: Документ з вимогами, що описує специфікації проєкту.
