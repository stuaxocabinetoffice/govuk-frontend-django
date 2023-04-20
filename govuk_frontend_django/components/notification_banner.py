from dataclasses import dataclass
from typing import Optional

from govuk_frontend_django.components import base as govuk_frontend_base
from govuk_frontend_django.components import (
    error_message as govuk_frontend_error_message,
)
from govuk_frontend_django.components import fieldset as govuk_frontend_fieldset
from govuk_frontend_django.components import hint as govuk_frontend_hint
from govuk_frontend_django.components import label as govuk_frontend_label
from govuk_frontend_django.components import tag as govuk_frontend_tag


@dataclass(kw_only=True)
class GovUKNotificationBanner(govuk_frontend_base.GovUKComponent):
    """GOV.UK Notification Banner

    See: https://design-system.service.gov.uk/components/notification-banner/
    """

    text: Optional[str] = None
    html: Optional[str] = None
    titleText: Optional[str] = None
    titleHtml: Optional[str] = None
    titleHeadingLevel: Optional[str] = None
    type: Optional[str] = None
    role: Optional[str] = None
    titleId: Optional[str] = None
    disableAutoFocus: Optional[bool] = None

    _jinja2_template = "govuk_frontend_jinja/components/notification-banner/macro.html"
    _macro_name = "govukNotificationBanner"


COMPONENT = GovUKNotificationBanner
