"""The Safe Mode integration."""
from homeassistant.components import persistent_notification
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType

DOMAIN = "safe_mode"

CONFIG_SCHEMA = cv.empty_config_schema(DOMAIN)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Safe Mode component."""
    persistent_notification.async_create(
        hass,
        (
            "Home Assistant is running in safe mode. Check [the error"
            " log](/config/logs) to see what went wrong."
        ),
        "Safe Mode",
    )
    return True
