from Clocko.settings import TEMPLATES

TEMPLATES[0]["OPTIONS"]["context_processors"].append(
    "Clocko_crumbs.context_processors.breadcrumbs",
)

