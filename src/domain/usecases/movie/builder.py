from .. import interfaces
from .create import CreateMovieUsecase
from .delete_by_id import DeleteMovieByIdUsecase
from .get_all import GetAllMoviesUsecase
from .get_all_reviews_by_id import GetAllMovieReviewsByIdUsecase
from .get_by_id import GetMovieByIdUsecase


class MovieUsecasesBuilder:
    def __init__(self, movie_repository: interfaces.repositories.MovieRepository) -> None:
        self._movie_repository = movie_repository

    def construct_create_movie_usecase(self) -> CreateMovieUsecase:
        return CreateMovieUsecase(movie_repository=self._movie_repository)

    def construct_delete_movie_by_id_usecase(self) -> DeleteMovieByIdUsecase:
        return DeleteMovieByIdUsecase(movie_repository=self._movie_repository)

    def construct_get_all_movie_reviews_by_id_usecase(self) -> GetAllMovieReviewsByIdUsecase:
        return GetAllMovieReviewsByIdUsecase(movie_repository=self._movie_repository)

    def construct_get_all_movies_usecase(self) -> GetAllMoviesUsecase:
        return GetAllMoviesUsecase(movie_repository=self._movie_repository)

    def construct_get_movie_by_id_usecase(self) -> GetMovieByIdUsecase:
        return GetMovieByIdUsecase(movie_repository=self._movie_repository)
