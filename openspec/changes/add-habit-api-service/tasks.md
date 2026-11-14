# Tasks

## 1. Контракт

- [ ] 1.1 Создать `api.yaml` (OpenAPI 3.0): пять операций `/habits`, схемы `Habit`, `HabitInput`, `HabitListResponse`, `Error`, `securitySchemes` Bearer, ответы 200/401/403/404, описания на русском. Проверка: `npx @openapitools/openapi-generator-cli validate -i api.yaml` завершается без ошибок.
- [ ] 1.2 Сверить контракт со спеками: каждая операция и каждый код из `specs/habits/spec.md` и `specs/api-auth/spec.md` присутствует в `api.yaml`. Проверка: ручной проход по таблице операций, расхождений нет.

## 2. Генерация каркаса

- [ ] 2.1 Сгенерировать сервис: `npx @openapitools/openapi-generator-cli generate -i api.yaml -g spring -o service`. Проверка: в `service/` появились `pom.xml`, интерфейс привычек в `src/main/java/**/api/`, четыре DTO в `src/main/java/**/model/`.
- [ ] 2.2 Зафиксировать в `README.md` команду генерации и версию генератора. Проверка: команда из `README.md` дословно совпадает с выполненной.

## 3. Рукописный слой

- [ ] 3.1 Реализовать `HabitStore`: `ConcurrentHashMap<String, Habit>`, сид из двух привычек с фиксированными `id` для `demo-user` и `other-user`. Проверка: класс компилируется в составе `mvn -q package`, сид-данные видны в ответе `GET /habits`.
- [ ] 3.2 Реализовать `HabitService`: список с фильтром `active` и подсчётом `total`, чтение, создание (UUID, `ownerId`, метки времени, `active` по умолчанию `true`), обновление и удаление с проверкой владения. Проверка: `GET /habits?active=true`, `POST /habits`, `PUT /habits/{habitId}` дают ожидаемые тела (см. 5.2).
- [ ] 3.3 Реализовать доменные исключения `HabitNotFound` и `HabitForbidden` плюс `@RestControllerAdvice`, собирающий `Error` с `status` и непустым `message`. Проверка: `GET /habits/{unknownId}` возвращает 404 и `Error` с полями `status`, `message`.
- [ ] 3.4 Реализовать `HabitController` как `@RestController`, реализующий сгенерированный интерфейс привычек; в генерируемые пакеты правок не вносить. Проверка: `git status` показывает изменения только в рукописном пакете `service`, генерируемые файлы не изменены.
- [ ] 3.5 Реализовать `HabitAuthFilter` (`OncePerRequestFilter`) и `WebMvcConfigurer`: разбор `Authorization: Bearer`, статическая карта `demo-token` → `demo-user` и `other-token` → `other-user`, `401` с телом `Error` при отсутствии/неизвестном токене, `ownerId` в атрибуте запроса. Проверка: запрос без заголовка даёт 401, запрос с `demo-token` — 200.

## 4. Сборка

- [ ] 4.1 Подготовить Maven вне `service/`: скачать `apache-maven-3.9.x` в `.tools/`. Проверка: `.tools/apache-maven-3.9.*/bin/mvn -v` с `JAVA_HOME` на JDK 16 печатает версию Maven и Java.
- [ ] 4.2 Собрать сервис: `mvn -q package` из `service/`. Проверка: `BUILD SUCCESS`, исполняемый jar в `service/target/`. Если JDK 16 не подходит — остановиться и согласовать с пользователем установку JDK 17 или проверку сборки на его машине.
- [ ] 4.3 Запустить сервис и прогнать сценарии из спек вручную: `GET /habits` (200), список с `active`-фильтром (200), `GET/PUT/DELETE` несуществующего (404), чужая привычка с `demo-token` (403), запрос без токена (401), полный цикл `POST` → `GET` → `PUT` → `DELETE` (200). Проверка: коды и тела ответов совпадают со спеками.

## 5. README

- [ ] 5.1 Написать `README.md` по структуре из `AGENTS.md`: что сгенерировано и чем, что написано руками, какие промпты/правки понадобились, как собрать и запустить, какие части — заглушки (хранение в памяти, статический токен), где расхождение по коду `400`. Проверка: каждая команда из `README.md` исполняется дословно; разделы покрывают все пункты структуры.

## Workflow follow-up

- Заархивировать изменение после проверки результата: `openspec archive add-habit-api-service`.
