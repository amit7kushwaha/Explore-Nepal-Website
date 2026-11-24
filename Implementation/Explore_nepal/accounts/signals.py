"""Admin access logging.  SRS: NFR-14 - log admin access WITHOUT passwords or sensitive form data."""
import logging

from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver

audit = logging.getLogger("accounts.audit")


def _ip(request):
    if request is None:
        return "unknown"
    return request.META.get("REMOTE_ADDR", "unknown")


@receiver(user_logged_in)
def log_login(sender, request, user, **kwargs):
    audit.info("LOGIN ok user=%s ip=%s", user.get_username(), _ip(request))


@receiver(user_logged_out)
def log_logout(sender, request, user, **kwargs):
    if user is not None:
        audit.info("LOGOUT user=%s ip=%s", user.get_username(), _ip(request))


@receiver(user_login_failed)
def log_login_failed(sender, credentials, request=None, **kwargs):
    # only the username is logged - NEVER the password
    audit.warning("LOGIN failed user=%s ip=%s", credentials.get("username", "?"), _ip(request))
