import punq

from core.apps.courses.services.courses import (
    BaseCourseService,
    ORMCourseService,
)
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

    return container
