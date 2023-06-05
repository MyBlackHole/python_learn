import warnings


warnings.warn(
    "The 'task_concurrency' parameter is deprecated. Please use 'max_active_tis_per_dag'.",
    None,
    stacklevel=2,
)
