from fastapi import APIRouter

from domain import usecases

from .routers import auth, dependencies, movies, reviews, users


def get_api_router(
    auth_usecases_builder: usecases.auth.AuthUsecasesBuilder,
    user_usecases_builder: usecases.user.UserUsecasesBuilder,
    movie_usecases_builder: usecases.movie.MovieUsecasesBuilder,
    review_usecases_builder: usecases.review.ReviewUsecasesBuilder,
) -> APIRouter:
    dependencies.usecases.auth.auth_usecases_builder = auth_usecases_builder
    dependencies.usecases.user.user_usecases_builder = user_usecases_builder
    dependencies.usecases.movie.movie_usecases_builder = movie_usecases_builder
    dependencies.usecases.review.review_usecases_builder = review_usecases_builder

    router = APIRouter()

    router.include_router(auth.router, prefix="/auth", tags=["auth"])
    router.include_router(users.router, prefix="/users", tags=["users"])
    router.include_router(movies.router, prefix="/movies", tags=["movies"])
    router.include_router(reviews.router, prefix="/reviews", tags=["reviews"])

    return router
