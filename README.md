## API Endpoints

1. **Создать запись**
   - POST `/entries/`
   - Body: `{"title": "string", "content": "string"}`

2. **Получить список записей**
   - GET `/entries/`
   - Параметры: `skip` (пропуск), `limit` (ограничение)

3. **Получить одну запись**
   - GET `/entries/{entry_id}`

4. **Обновить запись**
   - PUT `/entries/{entry_id}`
   - Body: `{"title": "string", "content": "string", "is_completed": boolean}`

5. **Удалить запись**
   - DELETE `/entries/{entry_id}`

6. **Пометить запись как выполненную/невыполненную**
   - PATCH `/entries/{entry_id}/complete`
   - Параметр: `completed=true/false`

