# История изменений

Все значимые изменения в проекте документируются в этом файле.

Формат основан на [Keep a Changelog](https://keepachangelog.com/ru/1.0.0/),
и проект следует [Semantic Versioning](https://semver.org/lang/ru/).

## [1.0.0] - 2025-07-29

### Добавлено
- Базовый функционал ипотечного калькулятора
- Расчет ежемесячного платежа по формуле аннуитета
- Генерация графика платежей
- Расчет переплаты по процентам
- Два режима расчета: "Кредит" и "Рассрочка"
- Функция досрочного погашения с двумя режимами:
  - Уменьшение ежемесячного платежа
  - Сокращение срока кредита
- Визуализация данных с помощью Chart.js
- Экспорт результатов в Excel
- Современный интерфейс с градиентным дизайном
- Адаптивная верстка для мобильных устройств
- Автоматическое форматирование чисел с разделителями
- Валидация входных данных
- Обработка ошибок с информативными сообщениями

### Технические особенности
- Использование Flask для веб-приложения
- Точные финансовые вычисления с помощью Decimal
- AJAX взаимодействие для динамических расчетов
- Создание Excel файлов с помощью openpyxl
- Полная документация кода и функций
- Подробные руководства пользователя и техническая документация

### Исправлено
- Корректный расчет года в графике платежей
- Правильный расчет экономии на процентах при досрочном погашении
- Исправление ошибок при повторных расчетах досрочного погашения
- Корректное отображение графиков сравнения

### Изменено
- Улучшен пользовательский интерфейс
- Добавлены анимации и визуальные эффекты
- Оптимизирована производительность расчетов
- Улучшена обработка ошибок

## [0.9.0] - 2025-07-28

### Добавлено
- Первоначальная версия ипотечного калькулятора
- Базовая функциональность расчета кредита
- Простой веб-интерфейс

---

## Планы на будущее

### [1.1.0] - Планируется
- Добавление дифференцированных платежей
- Расширенная аналитика и графики
- Сохранение истории расчетов
- Дополнительные типы кредитов

### [1.2.0] - Планируется
- Интеграция с банковскими API
- Мобильное приложение
- Многоязычность
- Расширенные отчеты

### [2.0.0] - Планируется
- Полная переработка архитектуры
- Микросервисная архитектура
- База данных для хранения данных
- REST API для интеграции 
