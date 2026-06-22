from fastapi import FastAPI
from app.modules.users.router import router as users_router
from app.modules.products.router import router as products_router
from app.modules.stocks.router import router as stocks_router
from app.modules.user_profiles.router import router as user_profile_router
app = FastAPI(title="Ecommerce Web API")

app.include_router(users_router, prefix="/api/v1")
# app.include_router(users_router, prefix="/api/v1")

app.include_router(products_router, prefix="/api/v1")
 
app.include_router(stocks_router, prefix="/api/v1")

app.include_router(user_profile_router, prefix="/api/v1")
 
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}
