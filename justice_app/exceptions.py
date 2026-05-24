class YouthRecordNotFound(Exception):
    """
    Raised when a requested youth record cannot be found.
    """
    pass


class RecommendationAccessDenied(Exception):
    """
    Raised when a user is not allowed to access recommendation logic.
    """
    pass


class RecommendationGenerationError(Exception):
    """
    Raised when support recommendation generation fails.
    """
    pass


class NoSupportProgramAvailable(Exception):
    """
    Raised when no matching support program is available for a youth.
    """
    pass