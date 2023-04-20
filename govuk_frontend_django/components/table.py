from dataclasses import dataclass
from typing import List, Optional

from govuk_frontend_django.components import base as govuk_frontend_base
from govuk_frontend_django.components import (
    error_message as govuk_frontend_error_message,
)
from govuk_frontend_django.components import fieldset as govuk_frontend_fieldset
from govuk_frontend_django.components import hint as govuk_frontend_hint
from govuk_frontend_django.components import label as govuk_frontend_label
from govuk_frontend_django.components import tag as govuk_frontend_tag


@dataclass(kw_only=True)
class TableHead:
    text: Optional[str] = None
    html: Optional[str] = None
    format: Optional[str] = None
    classes: Optional[str] = None
    colspan: Optional[int] = None
    rowspan: Optional[int] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class TableRows:
    text: Optional[str] = None
    html: Optional[str] = None
    format: Optional[str] = None
    classes: Optional[str] = None
    colspan: Optional[int] = None
    rowspan: Optional[int] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class GovUKTable(govuk_frontend_base.GovUKComponent):
    """GOV.UK Table

    See: https://design-system.service.gov.uk/components/table/
    """

    rows: List[List[TableRows]]
    head: Optional[List[TableHead]] = None
    caption: Optional[str] = None
    captionClasses: Optional[str] = None
    firstCellIsHeader: Optional[bool] = None

    _jinja2_template = "govuk_frontend_jinja/components/table/macro.html"
    _macro_name = "govukTable"


COMPONENT = GovUKTable
