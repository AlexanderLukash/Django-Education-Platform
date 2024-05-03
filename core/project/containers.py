import punq

from core.apps.courses.services.courses import (
    BaseCourseService,
    ORMCourseService,
)
from core.apps.courses.services.reviews import (
    BaseCourseReviewService,
    BaseCourseReviewValidator,
    CourseReviewValidatorService,
    ORMCourseReviewService,
)
from core.apps.courses.use_cases.reviews.create import CreateCourseReviewUseCase
from core.apps.members.services.auth import (
    AuthService,
    BaseAuthService,
)
from core.apps.members.services.codes import (
    BaseCodeService,
    DjangoCacheCodeService,
)
from core.apps.members.services.members import (
    BaseMemberService,
    ORMMemberService,
)
from core.apps.members.services.senders import (
    BaseSenderService,
    DummySenderService,
)


def get_container() -> punq.Container:
    return initialize_container()


def initialize_container() -> punq.Container:
    container = punq.Container()

    # initialize services
    container.register(BaseCourseService, ORMCourseService)
    container.register(BaseMemberService, ORMMemberService)
    container.register(BaseCodeService, DjangoCacheCodeService)
    container.register(BaseSenderService, DummySenderService)
    container.register(BaseAuthService, AuthService)
    container.register(BaseCourseReviewService, ORMCourseReviewService)
    container.register(BaseCourseReviewValidator, CourseReviewValidatorService)
    container.register(CreateCourseReviewUseCase)

    return container
