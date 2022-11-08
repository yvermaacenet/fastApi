from fastapi import FastAPI 
from database import engine
from routers import blog_router, globalnetwork_candidate_router,user_router, authentication_router
from models import blog_models ,globalnetwork_candidate_models, user_models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# <!================ create table when it's not exits in database ===============> 
blog_models.Base.metadata.create_all(bind=engine)
globalnetwork_candidate_models.Base.metadata.create_all(bind=engine) 
user_models.Base.metadata.create_all(bind=engine)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.include_router(authentication_router.router)
#app.include_router(blog_router.router)
app.include_router(globalnetwork_candidate_router.router)
app.include_router(user_router.router)