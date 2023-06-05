import logging.config

from logging import (
    LogRecord,
)


class AIOZeroDivisionError(Exception):
    def __init__(self):
        self.msg = "被除数为 0"

    def __str__(self):
        return repr(self.msg)


class MyLogRecord(LogRecord):
    def __init__(
        self,
        name,
        level,
        pathname,
        lineno,
        msg,
        args,
        exc_info,
        func=None,
        sinfo=None,
        **kwargs
    ) -> None:
        if exc_info is not None:
            if isinstance(exc_info[1], ZeroDivisionError):
                msg = "\n" + msg + "\n" + str(AIOZeroDivisionError())
        super().__init__(
            name,
            level,
            pathname,
            lineno,
            msg,
            args,
            exc_info,
            func,
            sinfo,
            **kwargs,
        )

    # def __init__(
    #     self,
    #     *args,
    #     **kw,
    # ) -> None:
    #     exc_info = kw.get("exc_info", None)
    #     if exc_info is not None:
    #         if isinstance(exc_info[1], ZeroDivisionError):
    #             msg = AIOZeroDivisionError()
    #             kw["msg"] = msg

    #     super().__init__(
    #         *args,
    #         **kw,
    #     )

    def __repr__(self):
        return '<LogRecord: %s, %s, %s, %s, "%s">' % (
            self.name,
            self.levelno,
            self.pathname,
            self.lineno,
            self.msg,
        )

    def getMessage(self):
        """
        Return the message for this LogRecord.

        Return the message for this LogRecord after merging any user-supplied
        arguments with the message.
        """
        msg = str(self.msg)
        if self.args:
            msg = msg % self.args
        return msg


# class FileHandler(StreamHandler):
#     """
#     A handler class which writes formatted logging records to disk files.
#     """

#     def __init__(self, filename, mode="a", encoding=None, delay=False, errors=None):
#         """
#         Open the specified file and use it as the stream for logging.
#         """
#         # Issue #27493: add support for Path objects to be passed in
#         filename = os.fspath(filename)
#         # keep the absolute path, otherwise derived classes which use this
#         # may come a cropper when the current directory changes
#         self.baseFilename = os.path.abspath(filename)
#         self.mode = mode
#         self.encoding = encoding
#         if "b" not in mode:
#             self.encoding = io.text_encoding(encoding)
#         self.errors = errors
#         self.delay = delay
#         # bpo-26789: FileHandler keeps a reference to the builtin open()
#         # function to be able to open or reopen the file during Python
#         # finalization.
#         self._builtin_open = open
#         if delay:
#             # We don't open the stream, but we still need to call the
#             # Handler constructor to set level, formatter, lock etc.
#             Handler.__init__(self)
#             self.stream = None
#         else:
#             StreamHandler.__init__(self, self._open())

#     def close(self):
#         """
#         Closes the stream.
#         """
#         self.acquire()
#         try:
#             try:
#                 if self.stream:
#                     try:
#                         self.flush()
#                     finally:
#                         stream = self.stream
#                         self.stream = None
#                         if hasattr(stream, "close"):
#                             stream.close()
#             finally:
#                 # Issue #19523: call unconditionally to
#                 # prevent a handler leak when delay is set
#                 # Also see Issue #42378: we also rely on
#                 # self._closed being set to True there
#                 StreamHandler.close(self)
#         finally:
#             self.release()

#     def _open(self):
#         """
#         Open the current base file with the (original) mode and encoding.
#         Return the resulting stream.
#         """
#         open_func = self._builtin_open
#         return open_func(
#             self.baseFilename, self.mode, encoding=self.encoding, errors=self.errors
#         )

#     def emit(self, record):
#         """
#         Emit a record.

#         If the stream was not opened because 'delay' was specified in the
#         constructor, open it before calling the superclass's emit.

#         If stream is not open, current mode is 'w' and `_closed=True`, record
#         will not be emitted (see Issue #42378).
#         """
#         if self.stream is None:
#             if self.mode != "w" or not self._closed:
#                 self.stream = self._open()

#         if self.stream:
#             StreamHandler.emit(self, record)

#     def __repr__(self):
#         level = getLevelName(self.level)
#         return "<%s %s (%s)>" % (self.__class__.__name__, self.baseFilename, level)


config = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
        # 其他的 formatter
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "logging.log",
            "level": "DEBUG",
            "formatter": "simple",
        },
        "error_file": {
            "class": "logging.FileHandler",
            "filename": "logging.log",
            "level": "ERROR",
            "formatter": "simple",
        },
        # 其他的 handler
    },
    "loggers": {
        "StreamLogger": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
        "FileLogger": {
            # 既有 console Handler，还有 file Handler
            "handlers": ["error_file"],
            "level": "ERROR",
        },
        # 其他的 Logger
    },
}

if __name__ == "__main__":
    logging.config.dictConfig(config)
    StreamLogger = logging.getLogger("StreamLogger")
    FileLogger = logging.getLogger("FileLogger")
    print(logging._logRecordFactory)
    logging.setLogRecordFactory(MyLogRecord)
    print(logging._logRecordFactory)
    FileLogger.info("info")
    FileLogger.debug("debug")
    try:
        i = 1 / 0

    except Exception as e:
        FileLogger.exception("exception")
        # raise e
