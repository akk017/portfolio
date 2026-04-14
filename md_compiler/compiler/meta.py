from typing import Optional


class Meta:
    def __init__(self, title=None, slug=None, icon=None, source=None, links=None, date=None, watch=False) -> None:
        self._title = title
        self._slug = slug
        self._icon = icon
        self._source = source
        self._links = links
        self._date = date
        self._watch = watch

    @property
    def title(self) -> Optional[str]:
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = value

    @property
    def slug(self) -> Optional[str]:
        return self._slug

    @slug.setter
    def slug(self, value: str):
        self._slug = value

    @property
    def icon(self) -> Optional[str]:
        return self._icon

    @icon.setter
    def icon(self, value: str):
        self._icon = value

    @property
    def source(self) -> Optional[list[str]]:
        return self._source

    @source.setter
    def source(self, value: list[str]):
        self._source = value

    @property
    def links(self) -> Optional[list[str]]:
        return self._links

    @links.setter
    def links(self, value: list[str]):
        self._links = value

    @property
    def date(self) -> Optional[list[str]]:
        return self._date

    @date.setter
    def date(self, value: str):
        self._date = value