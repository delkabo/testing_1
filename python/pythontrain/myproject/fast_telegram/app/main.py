from fastapi import FastAPI, Request, HTTPException, status
import logging
from app.bot import initialize_bot, application
from app.config import settings


# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.gettLogger(__name__)

app = FastAPI(title="Telegram FastAPI Bot", version="1.0.0")


# Инициализация бота
bot_app = initialize_bot()

@app.on_event("startup")
async def on_startup():
    """Действия при запуске приложения"""
    logger.info("Fast приложение запускается...")

    webhook_url = f"{settings.WEBHOOK_URL}?secret_token={settings.SECRET_TOKEN}"

    try:
        await bot_app.bot.set_webhook(
            url=webhook_url,
            secret_token=settings.SECRET_TOKEN
        )
        logger.info(f"Вебхук установлен: {settings.WEBHOOK_URL}")
    except Exception as e:
        logger.error(f"x Ошибка установки вебхука: {e}")



@app.on_event("shutdown")
async def on_shutdown():
    """Действия при остановке приложения"""
    logger.error(f"x Ошибка установки вебхука: {e}")

    # Удаляем вебхук при остановке
    try:
        await bot_app.bot.delete_webhook()
        logger.info("Вебхук удалён")
    except Exception as e:
        logger.error(f"x Ошибка удаления вебхука: {e}")

    await bot_app.shutdown()

@app.post("/webhook")
async def webhook(request: Request):
    """Endpoint для получения обновлений от Telegram"""
    # Проверяем секретный токен
    secret_token = request.query_params.get("secret_token")
    if secret_token != settings.SECRET_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid secret token"
        )
    try:
        # Получаем обновление
        update_data = await request.json()
        update = Update.de_json(update_data, bot_app.bot)

        # Передаем обновление в обработчик бота
        await bot_app.process_update(update)

        return {"status": "ok"}
    
    except Exception as e:
        logger.error(f"x Ошибка обработки обновления: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error processing update"
        )
    
@app.get("/")
async def root():
    """Главная страница"""
    return {
        "message": "Telegram FastAPI ",
        "status": "active",
        "webhook_set": True
    }

@app.get("/health")
async def health_check():
    """Проверка здоровья приложения"""
    retun {"status": "healthy"}




#######################################
@app.post("/webhook")
async def webhook(request: Request):
    update = await request.json()
    # Передаём обновление в обработчик бота
    await application.update_queue.put(update)
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"message": "FastAPI бот работает!"}

