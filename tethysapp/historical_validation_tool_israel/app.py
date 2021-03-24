from tethys_sdk.base import TethysAppBase, url_map_maker


class HistoricalValidationToolIsrael(TethysAppBase):
    """
    Tethys app class for Historical Validation Tool Israel.
    """

    name = 'Historical Validation Tool Israel'
    index = 'historical_validation_tool_israel:home'
    icon = 'historical_validation_tool_israel/images/icon.gif'
    package = 'historical_validation_tool_israel'
    root_url = 'historical-validation-tool-israel'
    color = '#c0392b'
    description = ''
    tags = '"Hydrology", "Time Series", "Bias Correction", "Hydrostats", "GEOGloWS", "Historical Validation Tool"'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='historical-validation-tool-israel',
                controller='historical_validation_tool_israel.controllers.home'
            ),
        )

        return url_maps